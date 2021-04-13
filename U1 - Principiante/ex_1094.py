# https://www.urionlinejudge.com.br/judge/pt/problems/view/1094

from typing import Dict, List, NamedTuple
from enum import Enum


class Cobaia(Enum):
    SAPO = 'S'
    RATO = 'R'
    COELHO = 'C'
    NULO = ''

    @classmethod
    def create_cobaia(cls, value: str) -> 'Cobaia':
        if value in ('S', 'R', 'C'):
            return Cobaia(value)

        return Cobaia.NULO


class Teste(NamedTuple):
    quantity: int
    cobaia: Cobaia


def parse_input(entry: str) -> Teste:
    entry_values = entry.split()
    entry_qtd = int(entry_values[0])
    entry_cobaia = entry_values[1]

    cobaia = Cobaia.create_cobaia(entry_cobaia)
    return Teste(entry_qtd, cobaia)


qtd = int(input())
values: List[Teste] = [parse_input(input()) for _ in range(qtd)]


def group_quantity_by_cobaia(testes: List[Teste]) -> Dict[Cobaia, int]:

    result: Dict[Cobaia, int] = dict()

    for i in testes:

        if i.cobaia in result:
            result[i.cobaia] += i.quantity
        else:
            result[i.cobaia] = i.quantity

    return result


def calculate_percentage(sample: int, total: int) -> float:
    return 100.0 * (1.0 * sample) / (1.0 * total)


def calculate_total(values: List[int]) -> int:
    return sum(values)


grouped_value = group_quantity_by_cobaia(values)

total = calculate_total(list(grouped_value.values()))

coelhos = grouped_value[Cobaia.COELHO]
coelhos_percentage = calculate_percentage(coelhos, total)

ratos = grouped_value[Cobaia.RATO]
ratos_percentage = calculate_percentage(ratos, total)

sapos = grouped_value[Cobaia.SAPO]
sapos_percentage = calculate_percentage(sapos, total)

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhos_percentage:.2f} %')
print(f'Percentual de ratos: {ratos_percentage:.2f} %')
print(f'Percentual de sapos: {sapos_percentage:.2f} %')
