import pathlib
from collections import defaultdict

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day15_input.txt"

with open(base_dir / filename) as f:
    lines: list[str] = f.read().strip().split(",")

Lens = tuple[str, int]


def the_hash_algorithm(input: str) -> int:
    value = 0
    for char in input:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def find_lens_index_by_label(lenses: list[Lens], label: str) -> int:
    for i, lens in enumerate(lenses):
        if lens[0] == label:
            return i
    return -1


def part_1():
    return sum(the_hash_algorithm(line) for line in lines)


def part_2():
    boxes: defaultdict[int, list[Lens]] = defaultdict(list)

    for line in lines:
        if line.endswith("-"):
            label = line[:-1]
            box_number = the_hash_algorithm(label)
            box_lenses = boxes[box_number]

            lens_index = find_lens_index_by_label(box_lenses, label)
            if lens_index != -1:
                box_lenses.pop(lens_index)
        else:
            label, focal_length = line.split("=")
            focal_length = int(focal_length)
            lens = label, focal_length
            box_number = the_hash_algorithm(label)
            box_lenses = boxes[box_number]

            existing_lens_index = find_lens_index_by_label(box_lenses, label)

            if existing_lens_index == -1:
                box_lenses.append(lens)
            else:
                box_lenses[existing_lens_index] = lens

    focal_power = 0

    for box_number, box_lenses in boxes.items():
        for i, lens in enumerate(box_lenses, start=1):
            _, focal_length = lens
            focal_power += (box_number + 1) * focal_length * i

    return focal_power


print(f"{the_hash_algorithm('HASH')=}")
print(f"answer_p1 = {part_1()}")
print(f"answer_p1 = {part_2()}")
