# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

from typing import Tuple


def n(value: float, ballot: float) -> Tuple[int, float]:
    quantity = value // ballot
    result_value = value - quantity * ballot
    return int(quantity), result_value


value_input = float(input())

result = value_input

print('NOTAS:')
for ballot in [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]:
    value, result = n(result, ballot)
    print(f'{value} nota(s) de R$ {ballot:.2f}')


print('MOEDAS:')
for coin in [1.00, 0.50, 0.25, 0.1, 0.05, 0.01]:
    value, result = n(result, coin)
    print(f'{value} moeda(s) de R$ {coin:.2f}')
