import pathlib
from collections.abc import Iterable

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day13_input.txt"

with open(base_dir / filename) as f:
    lines: list[str] = f.read().splitlines()

Grid = list[list[str]]
grids: list[Grid] = []

grid: Grid = []

for line in lines:
    if line == "":
        if grid:
            grids.append(grid)
            grid = []
    else:
        grid.append(list(line))

if grid:
    grids.append(grid)


def print_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def get_sequence_symmetries(
    sequence: list[str],
    indices: Iterable[int],
) -> set[int]:
    width = len(sequence)
    symmetry: set[int] = set()

    for x in indices:
        comparison_width = min(x, width - x)
        start_a = max(0, x - comparison_width)
        end_a = x
        start_b = x
        end_b = x + comparison_width

        this_row = sequence[start_a:end_a]
        other_row = list(reversed(sequence[start_b:end_b]))

        if this_row == other_row:
            symmetry.add(x)

    return symmetry


def get_grid_score(grid: Grid, missing_allowed: int) -> int:
    width = len(grid[0])
    height = len(grid)

    row_symmetries = {k: 0 for k in set(range(1, width))}
    col_symmetries = {k: 0 for k in set(range(1, height))}

    for row in grid:
        symmetries = get_sequence_symmetries(row, row_symmetries)

        for k in symmetries:
            row_symmetries[k] += 1

    for col_idx in range(width):
        col = [row[col_idx] for row in grid]
        symmetries = get_sequence_symmetries(col, col_symmetries)
        for k in symmetries:
            col_symmetries[k] += 1

    if missing_allowed:
        for k, v in row_symmetries.items():
            if v == height - 1:
                return k
        for k, v in col_symmetries.items():
            if v == width - 1:
                return 100 * k

    for k, v in row_symmetries.items():
        if v == height:
            return k
    for k, v in col_symmetries.items():
        if v == width:
            return 100 * k

    return -9999999


def part_1():
    return sum(get_grid_score(grid, missing_allowed=0) for grid in grids)


def part_2():
    return sum(get_grid_score(grid, missing_allowed=1) for grid in grids)


print(f"answer_p1: {part_1()}")
print(f"answer_p2: {part_2()}")
