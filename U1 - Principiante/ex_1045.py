# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
from math import pow

values = input().split()
a = float(values[0])
b = float(values[1])
c = float(values[2])

a, b, c = sorted([a, b, c], reverse=True)

if a >= b + c:
    print('NAO FORMA TRIANGULO')

else:

    if pow(a, 2) == pow(b, 2) + pow(c, 2):
        print('TRIANGULO RETANGULO')
    elif pow(a, 2) > pow(b, 2) + pow(c, 2):
        print('TRIANGULO OBTUSANGULO')
    elif pow(a, 2) < pow(b, 2) + pow(c, 2):
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif any([a == b, a == c, b == c]):
        print('TRIANGULO ISOSCELES')
