# https://www.urionlinejudge.com.br/judge/pt/problems/view/1079

from typing import Tuple, NamedTuple


class Note(NamedTuple):
    value: float
    weight: float


input_qtd = int(input())


def resolve_input(entry: str) -> Tuple[float, float, float]:
    values = entry.split()
    v1 = float(values[0])
    v2 = float(values[1])
    v3 = float(values[2])
    return v1, v2, v3


values = [resolve_input(input()) for _ in range(input_qtd)]


def calculate_average(*note_values: Note) -> float:

    sum_note_weight = sum(x.value * x.weight for x in note_values)
    sum_weight = sum(x.weight for x in note_values)

    return sum_note_weight / sum_weight


weight_1 = 2.0
weight_2 = 3.0
weight_3 = 5.0

for i in values:
    result = calculate_average(
        Note(i[0], weight_1),
        Note(i[1], weight_2),
        Note(i[2], weight_3)
    )

    print(f'{result:.1f}')
