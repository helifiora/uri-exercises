# https://www.urionlinejudge.com.br/judge/pt/problems/view/1067

limit = int(input())

for x in range(1, limit + 1):
    if x % 2 != 0:
        print(x)
