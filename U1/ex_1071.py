# https://www.urionlinejudge.com.br/judge/pt/problems/view/1071

from typing import List


x = int(input())
y = int(input())

minor, major = (x, y) if x < y else (y, x)


def values_between(start: int, stop: int) -> List[int]:
    values = [x for x in range(start + 1, stop) if x % 2 != 0]
    return values


print(sum(values_between(minor, major)))
