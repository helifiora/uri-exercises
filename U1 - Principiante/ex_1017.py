# https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

km_per_liter = 12

hours = int(input())
velocity = int(input())

kms = velocity * hours
liters = kms / km_per_liter

print(f'{liters:.3f}')
