import os

def day2(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day2.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)

def is_safe(a):
    return all(x<y and 1 <= abs(y-x) <= 3 for x, y in zip(a, a[1:])) or all(x>y and 1 <= abs(y-x) <= 3 for x, y in zip(a, a[1:]))

def part1(f):
    res = 0
    for l in f:
        a = [int(i) for i in l.split(" ")]
        if is_safe(a):
            res += 1
    return res


def part2(f):
    res = 0
    for l in f:
        a = [int(i) for i in l.split(" ")]
        for i in range(len(a)):
            if is_safe(a[:i] + a[i+1:]):
                res += 1
                break
    
    return res