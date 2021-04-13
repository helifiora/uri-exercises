# https://www.urionlinejudge.com.br/judge/pt/problems/view/1074

x_qtd = int(input())

values = [int(input()) for _ in range(x_qtd)]


def type_of_number(value: int) -> str:

    if value == 0:
        return 'NULL'

    odd_even = 'ODD' if value % 2 != 0 else 'EVEN'
    positive_negative = 'POSITIVE' if value > 0 else 'NEGATIVE'
    return odd_even + ' ' + positive_negative


for i in values:
    print(type_of_number(i))
