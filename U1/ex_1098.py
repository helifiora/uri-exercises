# https://www.urionlinejudge.com.br/judge/pt/problems/view/1098

i = 0.0
j = 1.0 + i

stop = 2
repeat = 3

step = 0.2

while i <= stop:

    for index in range(repeat):
        if i == 0.00 or i == 1.00 or i == 2.00:
            print(f'I={i:.0f} J={j + index:.0f}')
        else:
            print(f'I={i:.1f} J={j + index:.1f}')

    i = round(i + step, 2)
    j = 1.0 + i
