# https://www.urionlinejudge.com.br/judge/pt/problems/view/1097

def create_sequence(start_i: int, step_i: int, start_j: int, step_j: int, repeat: int, stop: int):

    i = start_i
    j = start_j

    while i <= stop:

        for index in range(repeat):
            print(f'I={i} J={j - index}')

        i += step_i
        j += step_j


create_sequence(1, 2, 7, 2, 3, 10)
