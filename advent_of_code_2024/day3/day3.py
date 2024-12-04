import os
import re


def day3(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day3.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)
        

RE = r"\((\d+)\,(\d+)\)"
RE2 = r"(mul|do|don't)\(((\d+)\,(\d+))?\)"

def part1(f):
    sum = 0
    s = f.read().split("mul")
    for c in s:
        c = c[:c.find(")")+1]
        match = re.fullmatch(RE, c)
        if match:
            n1, n2 = map(int, match.groups())
            sum += n1 * n2

    return sum

        

def part2(f):
    sum = 0
    m = re.findall(RE2, f.read())
    do = True
    for s in m:
        if s[0] == "don\'t":
            do = False
        
        elif s[0] == "do":
            do = True

        else:
            if do:
                n1, n2 = map(int, s[2:])
                sum += n1 * n2
    return sum