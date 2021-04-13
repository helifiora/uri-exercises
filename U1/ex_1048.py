# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

from typing import Tuple


salary = float(input())


def calculate(salary: float) -> Tuple[float, int]:

    index = 0
    if salary < 0:
        index = 0
    elif salary <= 400.0:
        index = 15
    elif salary <= 800.0:
        index = 12
    elif salary <= 1200.0:
        index = 10
    elif salary <= 2000.0:
        index = 7
    else:
        index = 4

    return salary * (index / 100.0), index


adjust, index = calculate(salary)
new_salary = salary + adjust

print(f'Novo salario: {new_salary:.2f}')
print(f'Reajuste ganho: {adjust:.2f}')
print(f'Em percentual: {index} %')
