# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

name = input()

salary = float(input())
sales = float(input())

total = salary + sales * 0.15

print(f'TOTAL = R$ {total:.2f}')
