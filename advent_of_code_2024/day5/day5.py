import os

from functools import cmp_to_key

def day5(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day5.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)


def part1(f):
    res = 0
    d = {}
    for l in f:
        if l == "\n":
            break

        a, b = map(int, l.strip().split("|"))
        d.setdefault(a, set()).add(b)

    for l in f:
        if l == "\n" or "|" in l:
            continue

        a = [int(s) for s in l.split(",")]
        m = set()
        for i in a:
            if i in d.keys() and d[i] & m:
                break
            
            m.add(i)
            
        else:
            res += a[len(a)//2]
                
    return res


def part2(f):
    res = 0
    d = {}
    for l in f:
        if l == "\n":
            break

        a, b = map(int, l.strip().split("|"))
        d.setdefault(a, set()).add(b)


    for l in f:
        if l == "\n" or "|" in l:
            continue

        a = [int(s) for s in l.split(",")]
        m = set()
        for i in a:
            if i in d.keys() and d[i] & m:
                a.sort(key=cmp_to_key(lambda n, m: -1 if m in d[n] else 1 if n in d[m] else 0))
                res+=a[len(a)//2]
                break
            m.add(i)

    
    return res

