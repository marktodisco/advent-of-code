from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Self

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class CubeSet:
    red: int
    green: int
    blue: int

    @classmethod
    def from_text(cls, text: str) -> Self:
        # 3 green, 15 blue, 14 red
        [red_count] = re.compile(r"([+-]*\d+) red").findall(text) or ["0"]
        [green_count] = re.compile(r"([+-]*\d+) green").findall(text) or ["0"]
        [blue_count] = re.compile(r"([+-]*\d+) blue").findall(text) or ["0"]
        return cls(red=int(red_count), green=int(green_count), blue=int(blue_count))

    def is_possible(self) -> bool:
        is_red_possible = 0 <= self.red <= MAX_RED
        is_green_possible = 0 <= self.green <= MAX_RED
        is_blue_possible = 0 <= self.blue <= MAX_RED
        return is_red_possible and is_green_possible and is_blue_possible


@dataclass
class Game:
    id: int
    cube_sets: list[CubeSet]

    @classmethod
    def from_text(cls, text: str) -> Self:
        # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        game_id_text, game_text = text.split(":")
        cube_sets_text = game_text.split(";")

        [game_id] = re.compile(r"Game (\d+)").findall(game_id_text)
        cube_sets = [CubeSet.from_text(t) for t in cube_sets_text]

        return cls(id=int(game_id), cube_sets=cube_sets)

    def is_possible(self) -> bool:
        return all(cs.is_possible() for cs in self.cube_sets)


def main() -> None:
    file = "./data/day02/part1-testing.txt"

    with open(file, "r") as fp:
        lines = fp.read().strip().split("\n")

    print(lines)

    games = [Game.from_text(line) for line in lines]
    possible_games = list(filter(lambda game: game.is_possible(), games))
    ids = [game.id for game in possible_games]

    ids_total = sum(ids)
    print(f"{ids_total = }")


if __name__ == "__main__":
    main()
