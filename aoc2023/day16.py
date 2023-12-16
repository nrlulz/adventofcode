import pathlib
import sys
from dataclasses import dataclass

sys.setrecursionlimit(100000)


base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day16_input.txt"

with open(base_dir / filename) as f:
    lines: list[str] = f.read().splitlines()


@dataclass
class Direction:
    name: str
    dx: int
    dy: int

    def __hash__(self) -> int:
        return hash((self.dx, self.dy))


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other: Direction) -> "Position":
        return Position(self.x + other.dx, self.y + other.dy)

    def __hash__(self):
        return hash((self.x, self.y))


class Grid:
    def __init__(self, lines: list[list[str]]):
        self.height = len(lines)
        self.width = len(lines[0])
        self.cells = lines

    def validate_position(self, position: Position):
        if position.x < 0 or position.y < 0:
            raise IndexError(f"Out of bounds: {position.x=}, {position.y=}")
        if position.x >= self.width or position.y >= self.height:
            raise IndexError(f"Out of bounds: {position.x=}, {position.y=}")

    def count(self, ch: str) -> int:
        return sum(row.count(ch) for row in self.cells)

    def show(self):
        for row in self.cells:
            print("".join(row))
        print()

    def __getitem__(self, position: Position) -> str:
        self.validate_position(position)
        return self.cells[position.y][position.x]

    def __setitem__(self, position: Position, value: str):
        self.validate_position(position)
        self.cells[position.y][position.x] = value


directions = {
    "N": Direction("N", 0, -1),
    "E": Direction("E", 1, 0),
    "S": Direction("S", 0, 1),
    "W": Direction("W", -1, 0),
}
piece_directions = {
    ".": {
        "N": ("N",),
        "S": ("S",),
        "E": ("E",),
        "W": ("W",),
    },
    "-": {
        "N": ("W", "E"),
        "S": ("W", "E"),
        "E": ("E",),
        "W": ("W",),
    },
    "|": {
        "N": ("N"),
        "S": ("S"),
        "E": ("N", "S"),
        "W": ("N", "S"),
    },
    "/": {
        "N": ("E",),
        "S": ("W",),
        "E": ("N",),
        "W": ("S",),
    },
    "\\": {
        "N": ("W",),
        "S": ("E",),
        "E": ("S",),
        "W": ("N",),
    },
}


def energize_grid(
    grid: Grid,
    energized: Grid,
    position: Position,
    direction: Direction,
    seen: set[tuple[Position, Direction]] | None = None,
):
    if seen is None:
        seen = set()

    if (position, direction) in seen:
        return

    seen.add((position, direction))

    try:
        ch = grid[position]
    except IndexError:
        return

    energized[position] = "#"

    for direction_name in piece_directions[ch][direction.name]:
        new_direction = directions[direction_name]
        energize_grid(
            grid,
            energized,
            position + new_direction,
            new_direction,
            seen=seen,
        )


def part_1():
    grid = Grid([list(line) for line in lines])
    energized = Grid([["." for _ in range(grid.width)] for _ in range(grid.height)])
    energize_grid(grid, energized, Position(0, 0), directions["E"])
    return energized.count("#")


def part_2():
    best = 0
    grid = Grid([list(line) for line in lines])

    for x in range(grid.width):
        # top edge
        energized = Grid([["." for _ in range(grid.width)] for _ in range(grid.height)])
        energize_grid(grid, energized, Position(x, 0), directions["S"])
        best = max(best, energized.count("#"))

        # bottom edge
        energized = Grid([["." for _ in range(grid.width)] for _ in range(grid.height)])
        energize_grid(grid, energized, Position(x, grid.height - 1), directions["N"])
        best = max(best, energized.count("#"))

    for y in range(grid.height):
        # left edge
        energized = Grid([["." for _ in range(grid.width)] for _ in range(grid.height)])
        energize_grid(grid, energized, Position(0, y), directions["E"])
        best = max(best, energized.count("#"))

        # right edge
        energized = Grid([["." for _ in range(grid.width)] for _ in range(grid.height)])
        energize_grid(grid, energized, Position(grid.width - 1, y), directions["W"])
        best = max(best, energized.count("#"))

    return best


print(f"answer_p1 = {part_1()}")
print(f"answer_p2 = {part_2()}")
