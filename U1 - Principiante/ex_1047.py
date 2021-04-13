# https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

from typing import Tuple


values = input().split()
hour_initial = int(values[0])
min_initial = int(values[1])
hour_final = int(values[2])
min_final = int(values[3])


def calculate(h_initial, h_final, m_initial, m_final) -> Tuple[int, int]:
    minutes_total_final = h_final * 60 + m_final
    minutes_total_initial = h_initial * 60 + m_initial

    if h_initial == h_final and m_initial >= m_final or h_initial > h_final:
        diff = (24 * 60 - minutes_total_initial) + minutes_total_final
    else:
        diff = minutes_total_final - minutes_total_initial

    hours = diff // 60
    minutes = diff % 60
    return hours, minutes


hours, minutes = calculate(hour_initial, hour_final, min_initial, min_final)

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
