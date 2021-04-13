# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

value_input = input().split()
a = float(value_input[0])
b = float(value_input[1])
c = float(value_input[2])


def is_triangle(a: float, b: float, c: float) -> bool:
    c1 = abs(b - c) < a < b + c
    c2 = abs(a - c) < b < a + c
    c3 = abs(a - b) < c < a + b
    return any([c1, c2, c3])


def area(a: float, b: float, c: float) -> float:
    return (a + b) * c / 2.0


def perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


if is_triangle(a, b, c):
    print(f'Perimetro = {perimeter(a, b, c):.1f}')
else:
    print(f'Area = {area(a, b, c):.1f}')
