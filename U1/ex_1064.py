# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

from typing import List


v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

input_values = [v1, v2, v3, v4, v5, v6]


def is_positive(value: float) -> bool:
    return value >= 0.0


def mean(values: List[float]) -> float:
    sum_values = sum(values)
    qtd = len(values)
    return sum_values / qtd


positive_values = list(filter(is_positive, input_values))
positive_qtd = len(positive_values)
positive_mean = mean(positive_values)

print(f'{positive_qtd} valores positivos')
print(f'{positive_mean:.1f}')
