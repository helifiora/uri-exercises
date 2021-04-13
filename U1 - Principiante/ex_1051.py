# https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

from typing import Callable, Optional, NamedTuple, List
from functools import reduce

salary = float(input())


class Tax(NamedTuple):
    percent: float
    min_value: float
    max_value: Optional[float]


def tax_interval(value: float, vmin: float, vmax: Optional[float] = None) -> float:

    vmin_i = vmin
    if vmin_i != 0.0:
        vmin_i += 0.01

    if vmax and (vmin_i <= value <= vmax or value >= vmax):
        return min(vmax - vmin, value - vmin)

    elif not vmax and value > vmin:
        return value - vmin

    return 0.0


def reduce_taxes(value: float) -> Callable[[float, Tax], float]:

    def inside(svalue: float, tax: Tax) -> float:
        return svalue + tax_interval(value, tax.min_value, tax.max_value) * tax.percent

    return inside


def calculate_tax(value: float) -> float:

    taxes: List[Tax] = [
        Tax(0.0, 0.00, 2000.00),
        Tax(0.08, 2000.00, 3000.00),
        Tax(0.18, 3000.00, 4500.00),
        Tax(0.28, 4500.00, None)
    ]

    red = reduce_taxes(value)
    return reduce(red, taxes, 0.00)


value = calculate_tax(salary)
if value == 0.0:
    print('Isento')
else:
    print(f'R$ {value:.2f}')
