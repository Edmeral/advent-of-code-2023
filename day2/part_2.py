"""12 red cubes, 13 green cubes, and 14 blue cubes"""
import pathlib
from functools import reduce
from utils import read_file

path = pathlib.Path(__file__).parent / "input"
# path = pathlib.Path(__file__).parent / "input_example"
lines = read_file(path)


def min_cubes(line: str) -> tuple[int, bool]:
    game, set_str = line.split(":")
    game = int(game.split(" ")[1])
    sets = [set.strip() for set in set_str.strip().split(";")]
    counters = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in sets:
        cubes = [cube.strip() for cube in set.split(",")]
        for cube in cubes:
            n, color = cube.split(" ")
            counters[color] = max(int(n), counters[color])
    return counters


games = [min_cubes(game_entry) for game_entry in lines]
sum = reduce(
    lambda sum, game: sum + game["red"] * game["green"] * game["blue"], games, 0
)
print(sum)
