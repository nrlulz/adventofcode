import itertools
import math
import pathlib
import re

base_dir = pathlib.Path(__file__).parent

MoveMap = dict[str, tuple[str, str]]

keys_re = re.compile(r"(?P<key>\w+) = \((?P<left>\w+), (?P<right>\w+)\)")


def parse_input(filename: str):
    with open(base_dir / filename) as f:
        lines = f.read().splitlines()

    instructions, _, *lines = lines

    moves: MoveMap = {}

    for line in lines:
        match = keys_re.match(line)

        if not match:
            continue

        moves[match.group("key")] = (match.group("left"), match.group("right"))

    return instructions, moves


def pathlen(position: str, instructions: str, moves: MoveMap, end: str) -> int:
    n = 1

    for ch in itertools.cycle(instructions):
        direction = 0 if ch == "L" else 1
        position = moves[position][direction]

        if position.endswith(end):
            break

        n += 1

    return n


def part_1():
    instructions, moves = parse_input("day8_input.txt")
    return pathlen("AAA", instructions, moves, end="ZZZ")


def part_2():
    instructions, moves = parse_input("day8_input.txt")
    positions = [k for k in moves.keys() if k.endswith("A")]
    pathlens = [pathlen(p, instructions, moves, end="Z") for p in positions]
    return math.lcm(*pathlens)


print(f"answer_p1={part_1()}")
print(f"answer_p2={part_2()}")
