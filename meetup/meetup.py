import calendar


def meetup(year, month, week, day_of_week):
    week_day = dict(zip(list(calendar.day_name), range(7)))
    c = calendar.Calendar()
    days = [d for d in c.itermonthdates(year, month) if d.weekday() == week_day[day_of_week] and d.month == month]

    if week == 'teenth':
        return [d for d in days if 13 <= d.day < 20][0]

    if week == 'last':
        return days[-1]

    try:
        return days[int(week[0]) - 1]
    except IndexError: raise MeetupDayException('day does not exist')


class MeetupDayException(Exception): pass
