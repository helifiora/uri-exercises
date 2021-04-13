# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

from collections import namedtuple
from typing import Dict

Snack = namedtuple('Snack', ['code', 'specification', 'price'])

menu: Dict[int, Snack] = {
    1: Snack(1, 'Cachorro Quente', 4.00),
    2: Snack(2, 'X-Salada', 4.50),
    3: Snack(3, 'X-Bacon', 5.00),
    4: Snack(4, 'Torrada simples', 2.00),
    5: Snack(5, 'Regrigerante', 1.50)
}

input_value = input().split()
code = int(input_value[0])
quantity = int(input_value[1])

total = menu[code].price * quantity

print(f'Total: R$ {total:.2f}')
