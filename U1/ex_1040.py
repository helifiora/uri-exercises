# https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

notes = input().split()
n1 = float(notes[0])
n2 = float(notes[1])
n3 = float(notes[2])
n4 = float(notes[3])

med = ((n1 * 2.0) + (n2 * 3.0) + (n3 * 4.0) + (n4 * 1.0)) / 10.0

print(f'Media: {med:.1f}')
if med >= 7.0:
    print('Aluno aprovado.')
elif med >= 5:
    print('Aluno em exame.')
    exam = float(input())
    print(f'Nota do exame: {exam:.1f}')

    new_med = (med + exam) / 2.0
    if new_med >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {new_med:.1f}')

else:
    print('Aluno reprovado.')
