# https://www.urionlinejudge.com.br/judge/pt/problems/view/1096

def create_sequence(start_i: int, step_i: int, start_j: int, repeat: int, stop: int):

    i = start_i
    j = start_j

    while i <= stop:

        for r_index in range(repeat):
            print(f'I={i} J={j - r_index}')

        i += step_i


create_sequence(1, 2, 7, 3, 10)
