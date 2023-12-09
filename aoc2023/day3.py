import pathlib
from collections import defaultdict

base_dir = pathlib.Path(__file__).parent

with open(base_dir / "day3_input.txt") as f:
    lines = f.read().splitlines()

part_numbers: list[int] = []

not_symbols = ".0123456789"

part_numbers_by_gear_position: dict[tuple[int, int], list[int]] = defaultdict(list)


def is_symbol(char: str) -> bool:
    return char != "." and not char.isdigit()


def has_neighboring_symbol(
    number: int,
    left: int,
    right: int,
    top: int,
    bottom: int,
) -> bool:
    symbol_found = False
    i = top
    for line in lines[top:bottom]:
        j = left
        for ch in line[left:right]:
            if is_symbol(ch):
                symbol_found = True
            if ch == "*":
                part_numbers_by_gear_position[(i, j)].append(number)
            j += 1
        i += 1
    return symbol_found


for i, line in enumerate(lines):
    number_str = ""

    for j, ch in enumerate(line):
        if ch.isdigit():
            number_str += ch

        if j == len(line) - 1 or not ch.isdigit():
            if number_str:
                if j == len(line) - 1 and ch.isdigit():
                    left = j - len(number_str)
                else:
                    left = j - len(number_str) - 1

                left = max(left, 0)
                right = min(j + 1, len(line))
                top = max(i - 1, 0)
                bottom = min(i + 1, len(lines)) + 1

                number = int(number_str)

                if has_neighboring_symbol(number, left, right, top, bottom):
                    part_numbers.append(number)

            number_str = ""

answer_p1 = sum(part_numbers)
print(f"{answer_p1=}")

pairs = [pns for pns in part_numbers_by_gear_position.values() if len(pns) == 2]
ratios = [a * b for a, b in pairs]
answer_p2 = sum(ratios)
print(f"{answer_p2=}")
