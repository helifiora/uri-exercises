# https://www.urionlinejudge.com.br/judge/pt/problems/view/1026

while True:

    try:
        a, b = map(int, input().split())
        print(a ^ b)

    except EOFError:
        break
