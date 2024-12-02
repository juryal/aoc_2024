from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def is_safe(levels: list[int], tolerance: int = 0) -> bool:
    if levels[0] < levels[1]:
        direction_is_safe = lambda x, y: x < y
    else:
        direction_is_safe = lambda x, y: x > y
    for index, level in enumerate(levels[:-1]):
        nextlevel = levels[index + 1]
        if not direction_is_safe(level, nextlevel) or abs(level - nextlevel) > 3:
            if tolerance == 0:
                return False
            else:
                for x in range(len(levels)):
                    dampenedlevels = levels.copy()
                    dampenedlevels.pop(x)
                    if is_safe(dampenedlevels):
                        return True
                return False
    return True


def partone(puzzle: list[str]) -> int:
    safe_reports = 0
    for line in puzzle:
        levels = [int(x) for x in line.split()]
        if is_safe(levels):
            safe_reports += 1
    return safe_reports


def parttwo(puzzle: list[str]) -> int:
    safe_reports = 0
    for line in puzzle:
        levels = [int(x) for x in line.split()]
        if is_safe(levels, tolerance=1):
            safe_reports += 1
    return safe_reports


print(partone(get_raw_puzzle("puzzles/sample02.txt")))
print(partone(get_raw_puzzle("puzzles/puzzle02.txt")))
print(parttwo(get_raw_puzzle("puzzles/sample02.txt")))
print(parttwo(get_raw_puzzle("puzzles/puzzle02.txt")))
