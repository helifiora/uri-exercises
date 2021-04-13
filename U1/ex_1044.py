# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

values = input().split()
a = float(values[0])
b = float(values[1])

c1 = a % b == 0
c2 = b % a == 0

if any([c1, c2]):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
