# -*- coding: utf-8 -*-
from datetime import datetime
from typing import *
import re

# Const Variables
SUPPORTED_LOCALES: List[str] = ['en_US', 'nl_NL']
SUPPORTED_DATES_STR: List[str] = ['Date', 'Datum']
SUPPORTED_DATE_FORMATS = ('{month}/{day}/{year}', '{day}-{month}-{year}')
SUPPORTED_DESCRIPTIONS_STR: List[str] = ['Description', 'Omschrijving']
SUPPORTED_CHANGE_STR: List[str] = ['Change', 'Verandering']
SUPPORTED_CHANGE: List[str] = ['USD', 'EUR']
SUPPORTED_CURRENCY: Dict[str, str] = {'USD': '$', 'EUR': u'€'}
SUPPORTED_CURRENCY_FORMAT: List[Dict] = [str.maketrans('.,', ',.'), str.maketrans(',.', '.,')]
DATE_COL_LEN = 10
DESC_COL_LEN = 25
CHANGE_COL_LEN = 13


class LedgerEntry(object):
    def __init__(self, date: datetime, description: str, change: int):
        self.date: datetime = date
        self.description: str = description
        self.change: int = change

    def __lt__(self, other):
        if self.date < other.date:
            return True
        if self.date == other.date and self.change < other.change:
            return True
        if self.date == other.date and self.change == other.change and self.description < other.description:
            return True


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)

def get_locale_index(locale: str) -> int:
    if locale not in SUPPORTED_LOCALES: raise ValueError(f'Not Supported Locale: {locale}')
    return SUPPORTED_LOCALES.index(locale)


def format_header(locale_index: int) -> str:
    date = f'{SUPPORTED_DATES_STR[locale_index]:<{DATE_COL_LEN}}'
    description = f'{SUPPORTED_DESCRIPTIONS_STR[locale_index]:<{DESC_COL_LEN}}'
    change_type = f'{SUPPORTED_CHANGE_STR[locale_index]:<{CHANGE_COL_LEN}}'
    return ' | '.join((date, description, change_type))


def format_date(date: datetime, locale_index: int) -> str:
    return SUPPORTED_DATE_FORMATS[locale_index].format(
        day=f'{date.day:02}', month=f'{date.month:02}', year=f'{date.year:04}')


def format_description(description: str):
    if len(description) > DESC_COL_LEN:
        return f'{description[:DESC_COL_LEN - 3]}...'
    return f'{description:<{DESC_COL_LEN}}'


def format_change(change: int, currency: str, locale_index: int) -> str:
    if currency not in SUPPORTED_CHANGE: raise ValueError(f'Currency {currency} not supported.')
    if locale_index in [0]:
        is_negative = change < 0
        regex = re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\g<1>,', f'{SUPPORTED_CURRENCY[currency]}{abs(change) / 100:.2f}')
        return f'{f"({regex})":>13}' if is_negative else f"{regex + ' ':>13}"

    if locale_index in [1]:
        regex = re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\g<1>,', f'{SUPPORTED_CURRENCY[currency]} {change / 100:.2f}')
        return f"{regex + ' ':>13}".translate(SUPPORTED_CURRENCY_FORMAT[locale_index])

def format_entry(entry: LedgerEntry, locale_index: int, currency: str) -> str:
    date = format_date(entry.date, locale_index)
    description = format_description(entry.description)
    change = format_change(entry.change, currency, locale_index)
    return ' | '.join((date, description, change))

def format_entries(currency: str, locale: str, entries: List[LedgerEntry]) -> str:
    locale_index = get_locale_index(locale)
    return (format_header(locale_index)
            + ('\n' if entries else '')
            + '\n'.join(map(lambda x: format_entry(x, locale_index, currency), sorted(entries))))
