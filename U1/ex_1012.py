# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

entry = input().split()
a = float(entry[0])
b = float(entry[1])
c = float(entry[2])

pi = 3.14159

triangle_calc = (a * c) / 2.0
circle_calc = pi * c * c
trapezoid_calc = ((a + b) * c) / 2.0
square_calc = b * b
rectangle_calc = a * b

print(f'TRIANGULO: {triangle_calc:.3f}')
print(f'CIRCULO: {circle_calc:.3f}')
print(f'TRAPEZIO: {trapezoid_calc:.3f}')
print(f'QUADRADO: {square_calc:.3f}')
print(f'RETANGULO: {rectangle_calc:.3f}')
