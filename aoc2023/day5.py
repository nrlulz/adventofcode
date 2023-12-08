import pathlib
from collections import defaultdict

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day5_input.txt"

with open(base_dir / filename) as f:
    lines = f.read().splitlines()


class RangeMap:
    def __init__(self):
        self.ranges: dict[tuple[int, int], tuple[int, int]] = {}

    def add(self, source_start: int, dest_start: int, range_len: int):
        key = (source_start, source_start + range_len)
        value = (dest_start, dest_start + range_len)
        self.ranges[key] = value

    def get(self, source: int) -> int:
        for key, value in self.ranges.items():
            source_start, source_end = key
            dest_start, _ = value

            if source_start <= source < source_end:
                return dest_start + (source - source_start)

        return source

    def get_reverse(self, dest: int) -> int:
        for key, value in self.ranges.items():
            source_start, _ = key
            dest_start, dest_end = value

            if dest_start <= dest < dest_end:
                return source_start + (dest - dest_start)

        return dest


seeds_line, *lines = lines

seed_numbers_p1 = [int(n) for n in seeds_line.split(": ")[1].split()]

current_map = ""
maps: dict[str, RangeMap] = defaultdict(RangeMap)
map_names: list[str] = []

for line in lines:
    if not line:
        continue

    if line.endswith("map:"):
        current_map = line[:-1]
        map_names.append(current_map)
        continue

    numbers = [int(n) for n in line.split()]
    dest_start, source_start, range_len = numbers
    maps[current_map].add(source_start, dest_start, range_len)

seed_locations: list[int] = []

for seed_number in seed_numbers_p1:
    for map_name in map_names:
        seed_number = maps[map_name].get(seed_number)
    seed_locations.append(seed_number)

seed_ranges: list[tuple[int, int]] = []

for i in range(0, len(seed_numbers_p1), 2):
    start, count = seed_numbers_p1[i : i + 2]
    seed_ranges.append((start, start + count))


def seed_in_range(seed_number: int):
    for start, end in seed_ranges:
        if start <= seed_number < end:
            return True
    return False


answer_p1 = min(seed_locations)
print(f"{answer_p1=}")

location_number = 0

while True:
    seed_number = location_number
    path = [seed_number]

    for map_name in reversed(map_names):
        range_map = maps[map_name]
        seed_number = range_map.get_reverse(seed_number)
        path.append(seed_number)

    if seed_in_range(seed_number):
        break

    location_number += 1

print(f"answer_p2={location_number}")
