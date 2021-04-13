# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

values = input().split()
x = float(values[0])
y = float(values[1])

if x == y == 0.0:
    print('Origem')
elif x == 0.0:
    print('Eixo Y')
elif y == 0.0:
    print('Eixo X')
elif x > 0.0 and y > 0.0:
    print('Q1')
elif x < 0.0 and y > 0.0:
    print('Q2')
elif x < 0.0 and y < 0.0:
    print('Q3')
elif x > 0.0 and y < 0.0:
    print('Q4')
