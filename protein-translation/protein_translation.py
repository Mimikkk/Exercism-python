from itertools import islice
from typing import *
import re

dict_: Dict[Tuple[str], str] = {
    tuple(['AUG']): 'Methionine',
    tuple(['UUU', 'UUC']): 'Phenylalanine',
    tuple(['UUA', 'UUG']): 'Leucine',
    tuple(['UCU', 'UCC', 'UCA', 'UCG']): 'Serine',
    tuple(['UAU', 'UAC']): 'Tyrosine',
    tuple(['UGU', 'UGC']): 'Cysteine',
    tuple(['UGG']): 'Tryptophan',
    tuple(['UAA', 'UAG', 'UGA']): 'STOP'}

def find_protein(codon: str) -> str:
    if not codon: return ''

    for (key, value) in dict_.items():
        if codon in key:
            if value == 'STOP': return ''
            return value

def proteins(strand: str) -> List[str]:
    if len(strand) % 3 != 0: return []

    result: List[str] = []
    codons: Iter[str] = iter(re.findall(r'[A-Z]{3}', strand))
    while protein := find_protein(next(codons, '')):
        result.append(protein)
    return result
