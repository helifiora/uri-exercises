# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

from typing import Tuple


def ballot(value: int, ballot: int) -> Tuple[int, int]:
    quantity = value // ballot
    result_value = value - quantity * ballot
    return quantity, result_value


money = int(input())

ballot_100, result = ballot(money, 100)
ballot_50, result = ballot(result, 50)
ballot_20, result = ballot(result, 20)
ballot_10, result = ballot(result, 10)
ballot_5, result = ballot(result, 5)
ballot_2, result = ballot(result, 2)
ballot_1, result = ballot(result, 1)

print(money)
print(f'{ballot_100} nota(s) de R$ 100,00')
print(f'{ballot_50} nota(s) de R$ 50,00')
print(f'{ballot_20} nota(s) de R$ 20,00')
print(f'{ballot_10} nota(s) de R$ 10,00')
print(f'{ballot_5} nota(s) de R$ 5,00')
print(f'{ballot_2} nota(s) de R$ 2,00')
print(f'{ballot_1} nota(s) de R$ 1,00')
