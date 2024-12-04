import os

def day25(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day25.txt")
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

