import pathlib

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day14_input.txt"

Grid = list[list[str]]


def load_grid():
    with open(base_dir / filename) as f:
        lines: list[str] = f.read().splitlines()

    return [list(line) for line in lines]


def print_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def roll_rocks(from_row: list[str], to_row: list[str]) -> bool:
    width = len(from_row)
    rolled_rock = False
    for x in range(width):
        if from_row[x] == "O" and to_row[x] == ".":
            from_row[x] = "."
            to_row[x] = "O"
            rolled_rock = True
    return rolled_rock


def tilt_grid(grid: Grid, direction: str) -> Grid:
    width = len(grid[0])
    moved_rock = True

    while moved_rock:
        moved_rock = False

        if direction == "N":
            for y in range(1, len(grid)):
                upper_row = grid[y - 1]
                lower_row = grid[y]
                rolled_rock = roll_rocks(from_row=lower_row, to_row=upper_row)
                if rolled_rock:
                    moved_rock = True
        elif direction == "S":
            for y in range(len(grid) - 1, 0, -1):
                upper_row = grid[y - 1]
                lower_row = grid[y]
                rolled_rock = roll_rocks(from_row=upper_row, to_row=lower_row)
                if rolled_rock:
                    moved_rock = True
        elif direction == "E":
            for row in grid:
                for x in range(width - 1, 0, -1):
                    if row[x - 1] == "O" and row[x] == ".":
                        row[x] = "O"
                        row[x - 1] = "."
                        moved_rock = True
        elif direction == "W":
            for row in grid:
                for x in range(1, width):
                    if row[x - 1] == "." and row[x] == "O":
                        row[x] = "."
                        row[x - 1] = "O"
                        moved_rock = True
        else:
            raise ValueError(f"unknown direction: {direction}")

    return grid


def get_grid_load(grid: Grid) -> int:
    load = 0
    for y in range(len(grid)):
        row_multiplier = len(grid) - y
        n_rocks = sum(ch == "O" for ch in grid[y])
        load += n_rocks * row_multiplier
    return load


def hash_grid(grid: Grid) -> int:
    return hash(tuple(tuple(row) for row in grid))


def part_1():
    grid = load_grid()
    tilt_grid(grid, "N")
    return get_grid_load(grid)


def part_2():
    grid = load_grid()
    iterations = 1000000000
    grid_hashes: list[int] = []

    last_n_unique = 0
    exit_index = iterations
    cycle_window = 100

    for i in range(iterations):
        for direction in "NWSE":
            tilt_grid(grid, direction)

        grid_hashes.append(hash_grid(grid))

        if i % cycle_window == 0:
            n_unique = len(set(grid_hashes[-cycle_window:]))

            if n_unique == last_n_unique:
                exit_index = i + (iterations - i - 1) % n_unique

            last_n_unique = n_unique

        if i == exit_index:
            break

    return get_grid_load(grid)


print(f"answer_p1: {part_1()}")
print(f"answer_p2: {part_2()}")
