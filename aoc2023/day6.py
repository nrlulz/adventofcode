import math
import pathlib

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day6_input.txt"

with open(base_dir / filename) as f:
    lines = f.read().splitlines()


durations = [int(i) for i in lines[0].split(":").pop().split()]
distances = [int(i) for i in lines[1].split(":").pop().split()]
big_duration = int(lines[0].split(":").pop().replace(" ", ""))
big_distance = int(lines[1].split(":").pop().replace(" ", ""))


def get_n_ways(duration_ms: int, distance_mm: int) -> int:
    b = -duration_ms
    c = distance_mm
    discriminant = b**2 - 4 * c
    zero1 = (-b - discriminant**0.5) / 2
    zero2 = (-b + discriminant**0.5) / 2

    if zero1 % 1 == 0:
        zero1 += 1
    else:
        zero1 = math.ceil(zero1)

    if zero2 % 1 == 0:
        zero2 -= 1
    else:
        zero2 = math.floor(zero2)

    return zero2 - zero1 + 1


answer_p1 = 1
for duration_ms, distance_mm in zip(durations, distances):
    answer_p1 *= get_n_ways(duration_ms, distance_mm)

print(f"{answer_p1=}")

answer_p2 = get_n_ways(big_duration, big_distance)
print(f"{answer_p2=}")
