import os
from pathlib import Path


empty_day = """import os

def day%d(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day%d.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)


def part1(f):
    res = 0
    return res
                

def part2(f):
    res = 0
    return res

"""

for i in range(5, 26):
    if not Path(f"advent_of_code_2024/day{i}").exists():
        os.mkdir(f"advent_of_code_2024/day{i}")
    with open(Path(f"advent_of_code_2024/day{i}/day{i}.py"), "w") as f:
        f.write(empty_day % (i, i))