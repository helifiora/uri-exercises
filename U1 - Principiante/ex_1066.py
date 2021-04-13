# https://www.urionlinejudge.com.br/judge/pt/problems/view/1066
from functools import reduce

values = (int(input()) for _ in range(5))


class Classication:
    positive: int
    negative: int
    pair: int
    odd: int

    def __init__(self, positive: int, negative: int, pair: int, odd: int) -> None:
        self.positive = positive
        self.negative = negative
        self.pair = pair
        self.odd = odd


def is_pair(value: int) -> bool:
    return value % 2 == 0


def is_odd(value: int) -> bool:
    return not is_pair(value)


def is_positive(value: int) -> bool:
    return value > 0


def is_negative(value: int) -> bool:
    return value < 0


def gen_values(sum: Classication, current: int) -> Classication:

    if is_negative(current):
        sum.negative += 1

    elif is_positive(current):
        sum.positive += 1

    if is_odd(current):
        sum.odd += 1
    else:
        sum.pair += 1

    return sum


result = reduce(gen_values, values, Classication(0, 0, 0, 0))
print(f'{result.pair} valor(es) par(es)')
print(f'{result.odd} valor(es) impar(es)')
print(f'{result.positive} valor(es) positivo(s)')
print(f'{result.negative} valor(es) negativo(s)')
