# https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

i = 0
values = [0.0, 0.0]
while i < 2:

    value = float(input())
    if value < 0 or value > 10:
        print('nota invalida')
        continue

    values[i] = value
    i += 1


media = (values[0] + values[1]) / 2.0
print(f'media = {media:.2f}')
