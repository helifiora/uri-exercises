# https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

distance = int(input())
fuel = float(input())

km_per_liter = distance / fuel

print(f'{km_per_liter:.3f} km/l')
