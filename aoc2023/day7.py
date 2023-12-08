import pathlib
from collections import defaultdict

base_dir = pathlib.Path(__file__).parent
filename = base_dir / "day7_input.txt"

with open(base_dir / filename) as f:
    lines = f.read().splitlines()

label_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
hand_values = {
    "five_of_a_kind": 7,
    "four_of_a_kind": 6,
    "full_house": 5,
    "three_of_a_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1,
}


class Hand:
    cards: str
    card_values: tuple[int, ...]
    bid: int
    jokers_wild: bool

    def __init__(self, line: str, jokers_wild: bool):
        cards, bid = line.split()
        self.cards = cards
        self.card_values = tuple(label_values[c] for c in cards)
        self.bid = int(bid)
        self.jokers_wild = jokers_wild

    @property
    def hand_value(self):
        jokers = 0
        counts_by_label: dict[int, int] = defaultdict(int)
        for card in self.card_values:
            if self.jokers_wild and card == label_values["J"]:
                jokers += 1
                continue
            counts_by_label[card] += 1

        top_2_counts = sorted(counts_by_label.values(), reverse=True)[:2]
        if jokers == 5:
            return hand_values["five_of_a_kind"]

        top_2_counts[0] += jokers

        if top_2_counts[0] == 5:
            return hand_values["five_of_a_kind"]

        if top_2_counts[0] == 4:
            return hand_values["four_of_a_kind"]

        if top_2_counts == [3, 2]:
            return hand_values["full_house"]

        if top_2_counts[0] == 3:
            return hand_values["three_of_a_kind"]

        if top_2_counts == [2, 2]:
            return hand_values["two_pair"]

        if top_2_counts[0] == 2:
            return hand_values["one_pair"]

        return hand_values["high_card"]

    @property
    def sort_key(self):
        return (self.hand_value, *self.card_values)

    def __lt__(self, other: "Hand"):
        return self.sort_key < other.sort_key

    def __repr__(self):
        return f'Hand("{self.cards} {self.bid}", jokers_wild={self.jokers_wild})'


hands_p1: list[Hand] = sorted(Hand(line, jokers_wild=False) for line in lines)
answer_p1 = sum(hand.bid * (i + 1) for i, hand in enumerate(hands_p1))
print(f"{answer_p1=}")

label_values["J"] = 0
hands_p2: list[Hand] = sorted(Hand(line, jokers_wild=True) for line in lines)
answer_p2 = sum(hand.bid * (i + 1) for i, hand in enumerate(hands_p2))
print(f"{answer_p2=}")
