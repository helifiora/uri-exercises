# https://www.urionlinejudge.com.br/judge/pt/problems/view/1065
from array import array

v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

input_values = array('i', [v1, v2, v3, v4, v5])


def is_pair(value: int) -> bool:
    return value % 2 == 0


pair_values = list(filter(is_pair, input_values))
pair_qtd = len(pair_values)

print(f'{pair_qtd} valores pares')
