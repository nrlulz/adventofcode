import pathlib

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day4_input.txt"

with open(base_dir / filename) as f:
    lines = f.read().splitlines()

score = 0
n_cards = [1 for _ in lines]

for i, line in enumerate(lines):
    _, numbers = line.split(":")
    winning, have = numbers.split(" | ")

    winning_numbers = {int(n) for n in winning.split()}
    have_numbers = {int(n) for n in have.split()}

    have_winning_numbers = winning_numbers & have_numbers
    n_matches = len(have_winning_numbers)

    if n_matches:
        score += 2 ** (n_matches - 1)

    j = i + 1
    for __ in range(n_matches):
        if j >= len(lines):
            break
        n_cards[j] += n_cards[i]
        j += 1

answer_p1 = score
print(f"{answer_p1=}")

answer_p2 = sum(n_cards)
print(f"{answer_p2=}")
