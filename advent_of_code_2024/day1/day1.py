import bisect
import os

from collections import Counter

def day1(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day1.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)

def part1(f):
    a1 = []
    a2 = []
    for l in f:
        n, m = map(int, l.split("   "))
        bisect.insort(a1, n)
        bisect.insort(a2, m)
    res = sum(abs(n - m) for n, m in zip(a1, a2))
    return res

        
def part2(f):
    a1 = []
    a2 = []
    for l in f:
        n, m = map(int, l.split("   "))
        bisect.insort(a1, n)
        bisect.insort(a2, m)
    c = Counter(a2)
    res = sum(i * c[i] for i in a1)
    print(res)