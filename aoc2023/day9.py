import pathlib

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day9_input.txt"

with open(base_dir / filename) as f:
    lines = f.read().splitlines()

histories = [[int(n) for n in line.split()] for line in lines]

answer_p1 = 0
answer_p2 = 0

for history in histories:
    deltas: list[list[int]] = []
    last_line: list[int] = history

    while any(last_line):
        deltas.append(last_line)
        last_line = [last_line[i] - last_line[i - 1] for i in range(1, len(last_line))]

    first_value = 0
    last_value = 0
    for delta_list in reversed(deltas):
        last_value = delta_list[-1] + last_value
        first_value = delta_list[0] - first_value

    answer_p1 += last_value
    answer_p2 += first_value

print(f"{answer_p1=}")
print(f"{answer_p2=}")
