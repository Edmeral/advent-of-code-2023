import re
from utils import read_file
import pathlib

# path = pathlib.Path(__file__).parent / "input_example"
path = pathlib.Path(__file__).parent / "input"
lines = read_file(path)

numbers = []


def build_adjacent_position(line_idx: int, start_idx: int, end_idx):
    before_row = [(line_idx - 1, start_idx - 1)]
    for i in range(start_idx, end_idx + 1):
        before_row.append((line_idx - 1, i))

    in_row = [(line_idx, start_idx - 1), (line_idx, end_idx)]

    after_row = [(line_idx + 1, start_idx - 1)]
    for i in range(start_idx, end_idx + 1):
        before_row.append((line_idx + 1, i))

    return [*before_row, *in_row, *after_row]


star_numbers = []
non_gear_numbers = []
for i, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        is_adjacent = False
        number = int(match.group())
        start = match.start()
        end = match.end()
        adjacency_positions = build_adjacent_position(i, match.start(), match.end())
        for line_idx, str_index in adjacency_positions:
            try:
                if line_idx == -1 or str_index == -1:
                    continue
                if lines[line_idx][str_index] == "*":
                    # Could use a hash table to the position of the star tuple
                    # to make the gear ration calculation easier at the end
                    star_numbers.append(
                        {"number": number, "pos": (line_idx, str_index)}
                    )
            except KeyError:
                pass
            except IndexError:
                pass

gears_ratio_sum = 0
for star_number in star_numbers:
    for other_star_number in star_numbers:
        if other_star_number == star_number:
            continue
        if other_star_number["pos"] == star_number["pos"]:
            gears_ratio_sum += star_number["number"] * other_star_number["number"]

print(gears_ratio_sum // 2)
