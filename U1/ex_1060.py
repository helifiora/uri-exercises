# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())


def is_positive(value: float) -> bool:
    return value >= 0.0


positive = len(list(filter(is_positive, (v1, v2, v3, v4, v5, v6))))
print(f'{positive} valores positivos')
