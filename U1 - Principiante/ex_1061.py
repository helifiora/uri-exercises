# https://www.urionlinejudge.com.br/judge/pt/problems/view/1061

from typing import Tuple


start_day = int(input().split(' ')[1])
start_time = input().split(' : ')

end_day = int(input().split(' ')[1])
end_time = input().split(' : ')


def time_to_seconds(hour: int, minute: int, second: int) -> int:
    hour_to_second = hour * 60 * 60
    min_to_second = minute * 60
    return hour_to_second + min_to_second + second


def seconds_to_time(seconds: int) -> Tuple[int, int, int, int]:
    days = seconds // 86400
    seconds -= days * 86400

    hours = seconds // 3600
    seconds -= hours * 3600

    minutes = seconds // 60
    seconds -= minutes * 60

    return days, hours, minutes, seconds


start_total_seconds = time_to_seconds(
    int(start_time[0]),
    int(start_time[1]),
    int(start_time[2]))

end_total_seconds = time_to_seconds(
    int(end_time[0]),
    int(end_time[1]),
    int(end_time[2]))


diff_day_seconds = (end_day - start_day) * 24 * 3600
diff_time_seconds = end_total_seconds - start_total_seconds

day, hour, minute, second = seconds_to_time(
    diff_day_seconds + diff_time_seconds)

print(f'{day} dia(s)')
print(f'{hour} hora(s)')
print(f'{minute} minuto(s)')
print(f'{second} segundo(s)')
