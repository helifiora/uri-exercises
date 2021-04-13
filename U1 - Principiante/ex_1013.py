# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

entry = input().split()
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])


def higher(a: int, b: int) -> int:
    return int((a + b + abs(a - b)) / 2)


ab = higher(a, b)
abc = higher(ab, c)

print(f'{abc} eh o maior')
