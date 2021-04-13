# https://www.urionlinejudge.com.br/judge/pt/problems/view/1075

n = int(input())

for i in range(1, 10000 + 1):
    if i % n == 2:
        print(i)
