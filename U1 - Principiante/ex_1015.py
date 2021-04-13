# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

from math import sqrt, pow

p1 = input().split()
p1_x, p1_y = float(p1[0]), float(p1[1])

p2 = input().split()
p2_x, p2_y = float(p2[0]), float(p2[1])

distance = sqrt(pow(p2_x - p1_x, 2) + pow(p2_y - p1_y, 2))
print(f'{distance:.4f}')
