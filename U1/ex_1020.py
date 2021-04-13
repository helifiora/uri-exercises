# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

from typing import Tuple


days_input = int(input())


def n(value: int, days: int) -> Tuple[int, int]:
    quantity = value // days
    result = value - quantity * days
    return quantity, result


years, result = n(days_input, 365)
months, result = n(result, 30)
days = result

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
