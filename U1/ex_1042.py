# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042


values = input().split()
n1 = int(values[0])
n2 = int(values[1])
n3 = int(values[2])


for n in sorted([n1, n2, n3]):
    print(n)

print()


for n in [n1, n2, n3]:
    print(n)
