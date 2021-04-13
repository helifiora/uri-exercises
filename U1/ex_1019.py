# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

n = int(input())

hour = n // 3600

n -= hour * 3600

minutes = n // 60

n -= minutes * 60

seconds = n

print(f'{hour}:{minutes}:{seconds}')
