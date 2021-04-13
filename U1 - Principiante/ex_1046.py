# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

values = input().split()
start = int(values[0])
end = int(values[1])


def calculate_hours(start: int, end: int) -> int:
    if start < end:
        return end - start
    else:
        return (24 - start) + end


hours = calculate_hours(start, end)
print(f'O JOGO DUROU {hours} HORA(S)')
