"""12 red cubes, 13 green cubes, and 14 blue cubes"""
import pathlib
from utils import read_file

INITIAL_CUBES = {"red": 12, "green": 13, "blue": 14}

path = pathlib.Path(__file__).parent / "input"
# path = pathlib.Path(__file__).parent / "input_example"
lines = read_file(path)


def is_possible(line: str) -> tuple[int, bool]:
    game, set_str = line.split(":")
    game = int(game.split(" ")[1])
    sets = [set.strip() for set in set_str.strip().split(";")]
    for set in sets:
        counters = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        cubes = [cube.strip() for cube in set.split(",")]
        for cube in cubes:
            n, color = cube.split(" ")
            counters[color] += int(n)
        for color, n in counters.items():
            if counters[color] > INITIAL_CUBES[color]:
                return game, False
    return game, True


games = [is_possible(game_entry) for game_entry in lines]
valid_games = [game[0] for game in games if game[1]]
print(sum(valid_games))
