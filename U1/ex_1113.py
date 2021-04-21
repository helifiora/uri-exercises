# https://www.urionlinejudge.com.br/judge/pt/problems/view/1113
while True:

    x, y = tuple(int(x) for x in input().split())
    if x == y:
        break

    if x > y:
        print('Decrescente')
    else:
        print('Crescente')
