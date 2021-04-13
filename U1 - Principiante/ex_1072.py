# https://www.urionlinejudge.com.br/judge/pt/problems/view/1072

from typing import List, Tuple
from functools import reduce

entry_qtd = int(input())

values = [int(input()) for _ in range(entry_qtd)]


def exec_interval(interval: Tuple[int, int], values: List[int]) -> Tuple[int, int]:

    def exec_reduce(sum_value: Tuple[int, int], current: int) -> Tuple[int, int]:
        if interval[0] <= current <= interval[1]:
            return sum_value[0] + 1, sum_value[1]
        else:
            return sum_value[0], sum_value[1] + 1

    return reduce(exec_reduce, values, (0, 0))


in_value, out_value = exec_interval((10, 20), values)
print(f'{in_value} in')
print(f'{out_value} out')
