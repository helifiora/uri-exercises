# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

a = input().split(' ')
a_code = a[0]
a_units = int(a[1])
a_unit_value = float(a[2])

b = input().split(' ')
b_code = b[0]
b_units = int(b[1])
b_unit_value = float(b[2])

total = (a_units * a_unit_value) + (b_units * b_unit_value)

print(f'VALOR A PAGAR: R$ {total:.2f}')
