# https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

correct_password = '2002'

while True:

    password = input()
    if password == correct_password:
        print('Acesso Permitido')
        break

    print('Senha Invalida')
