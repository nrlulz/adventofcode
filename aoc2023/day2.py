from dataclasses import dataclass

with open("day2_input.txt") as f:
    lines = f.read().splitlines()


@dataclass
class GameSubset:
    red: int = 0
    green: int = 0
    blue: int = 0

    @property
    def is_possible(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    @property
    def power(self):
        return self.red * self.green * self.blue


@dataclass
class Game:
    id: int
    subsets: list[GameSubset]

    @property
    def is_possible(self):
        return all(subset.is_possible for subset in self.subsets)

    @property
    def minimum_subset(self):
        return GameSubset(
            red=max(s.red for s in self.subsets),
            green=max(s.green for s in self.subsets),
            blue=max(s.blue for s in self.subsets),
        )


games: list[Game] = []

for line in lines:
    game_id, rest = line.split(":")
    _, game_id = game_id.split()

    subsets: list[GameSubset] = []

    for subset in rest.split("; "):
        kwargs = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        cube_amounts = subset.split(", ")
        for amount_and_color in cube_amounts:
            n_cubes, color = amount_and_color.split()
            kwargs[color] += int(n_cubes)

        subsets.append(GameSubset(**kwargs))

    game = Game(id=int(game_id), subsets=subsets)
    games.append(game)

possible_games = [g for g in games if g.is_possible]
answer_p1 = sum(g.id for g in possible_games)
answer_p2 = sum(g.minimum_subset.power for g in games)
print(f"{answer_p1=}")
print(f"{answer_p2=}")
