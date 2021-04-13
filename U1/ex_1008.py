# https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

number = int(input())
hours = int(input())

salary_per_hour = float(input())

salary = hours * salary_per_hour

print(f'NUMBER = {number}')
print(f'SALARY = U$ {salary:.2f}')
