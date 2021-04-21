# https://www.urionlinejudge.com.br/judge/pt/problems/view/1099
from typing import Iterator, NamedTuple


class Limit(NamedTuple):
    lower: int
    higher: int


def get_odd_numbers_between_limit(limit: Limit) -> Iterator[int]:
    return filter(lambda value: value % 2 != 0, range(limit.lower + 1, limit.higher))


def transform_input_to_limit(value: str) -> Limit:
    x, y = tuple(int(x) for x in value.split(' '))
    l, h = (x, y) if x < y else (y, x)
    return Limit(int(l), int(h))


n = int(input())

value_limits = tuple(transform_input_to_limit(input()) for _ in range(n))

for limit in value_limits:
    odd_numbers = get_odd_numbers_between_limit(limit)
    sum_odd_numbers = sum(odd_numbers)
    print(sum_odd_numbers)
