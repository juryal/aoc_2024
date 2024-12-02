from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def partone(puzzle: list[str]) -> int:
    leftlist: list[int] = []
    rightlist: list[int] = []
    for line in puzzle:
        left, right = line.split()
        leftlist.append(int(left))
        rightlist.append(int(right))
    leftlist.sort()
    rightlist.sort()
    totaldifference: int = 0
    for index, value in enumerate(leftlist):
        totaldifference += abs(value - rightlist[index])
    return totaldifference


def parttwo(puzzle: list[str]) -> int:
    leftlist: list[int] = list()
    rightdict: dict[int, int] = dict()
    for line in puzzle:
        left, right = line.split()
        leftlist.append(int(left))
        rightint = int(right)
        try:
            rightdict[rightint] = rightdict[rightint] + 1
        except:
            rightdict[rightint] = 1
    total = 0
    for id in leftlist:
        total += id * rightdict.get(id, 0)
    return total


print(partone(get_raw_puzzle("puzzles/sample01.txt")))
print(partone(get_raw_puzzle("puzzles/puzzle01.txt")))
print(parttwo(get_raw_puzzle("puzzles/sample01.txt")))
print(parttwo(get_raw_puzzle("puzzles/puzzle01.txt")))
