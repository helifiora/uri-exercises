# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

from typing import Tuple
from math import pow, sqrt

input_values = input().split()
input_a = float(input_values[0])
input_b = float(input_values[1])
input_c = float(input_values[2])


def bhaskara(a: float, b: float, c: float) -> Tuple[bool, Tuple[float, float]]:

    if a == 0:
        return False, None

    delta = pow(b, 2) - (4 * a * c)
    if delta < 0:
        return False, None

    root = sqrt(delta)

    r1 = (-b + root) / (2 * a)
    r2 = (-b - root) / (2 * a)

    return True, (r1, r2)


result, roots = bhaskara(input_a, input_b, input_c)
if not result:
    print('Impossivel calcular')
else:
    r1 = roots[0]
    r2 = roots[1]
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
