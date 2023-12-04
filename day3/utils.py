import pathlib
def read_file(path: pathlib.Path) -> list[str]:
    lines = list[str]
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
