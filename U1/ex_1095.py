# https://www.urionlinejudge.com.br/judge/pt/problems/view/1095

def create_sequence(start_i: int, step_i: int, start_j: int, step_j: int):

    i = start_i
    j = start_j

    print(f'I={i} J={j}')

    while j > 0:
        i += step_i
        j -= step_j

        print(f'I={i} J={j}')


create_sequence(1, 3, 60, 5)
