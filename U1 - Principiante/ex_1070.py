# https://www.urionlinejudge.com.br/judge/pt/problems/view/1070

from typing import List


x = int(input())


def odd_numbers(qtd: int, start: int) -> List[int]:
    values_qtd = 0
    values = []
    i = start
    while values_qtd < qtd:
        if i % 2 != 0:
            values_qtd += 1
            values.append(i)

        i += 1

    return values


for i in odd_numbers(6, x):
    print(i)
