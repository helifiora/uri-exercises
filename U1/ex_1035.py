# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

value = input().split()
a = int(value[0])
b = int(value[1])
c = int(value[2])
d = int(value[3])


def is_pair(value: int) -> bool:
    return value % 2 == 0


def is_greater(value: int, than: int) -> bool:
    return value > than


def is_positive(value: int) -> bool:
    return value >= 0


result = is_greater(b, c) \
    and is_greater(d, a) \
    and is_greater(c + d, a + b) \
    and is_positive(c) \
    and is_positive(d) \
    and is_pair(a)

if result:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
