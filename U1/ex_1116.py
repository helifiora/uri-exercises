# https://www.urionlinejudge.com.br/judge/pt/problems/view/1116

n = int(input())

for _ in range(n):
    x, y = tuple(int(v) for v in input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x / y:.1f}')
