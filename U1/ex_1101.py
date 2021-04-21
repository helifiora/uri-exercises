# https://www.urionlinejudge.com.br/judge/pt/problems/view/1101
from typing import NamedTuple, Iterator


class Limit(NamedTuple):
    lower: int
    higher: int


def generate_sequence_interval(limit: Limit) -> range:
    return range(limit.lower, limit.higher + 1)


def has_zero_or_negative(limit: Limit) -> bool:
    return limit.lower <= 0 or limit.higher <= 0


def read_input(input_value: str) -> Limit:
    m, n = tuple(int(x) for x in input_value.split(' '))
    l, h = (m, n) if m < n else (n, m)
    return Limit(l, h)


while True:

    limit = read_input(input())
    if has_zero_or_negative(limit):
        break

    sequence_values = list(generate_sequence_interval(limit))
    sequence_sum = sum(sequence_values)

    sequence_str = ' '.join(str(x) for x in sequence_values)
    print(f'{sequence_str} Sum={sequence_sum}')
