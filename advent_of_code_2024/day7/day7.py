import os

def day7(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day7.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)
        
def concat(n, m):
    return int(str(n)+str(m))


def part1_helper(eqn, curr_num, eqn_idx):
    if eqn_idx == len(eqn):
        if curr_num == eqn[0]:
            return True
        
        else:
            return False

    if curr_num > eqn[0]:
        return False
    
    return part1_helper(eqn, curr_num * eqn[eqn_idx], eqn_idx+1) or part1_helper(eqn, curr_num + eqn[eqn_idx], eqn_idx+1)
    


def part1(f):
    res = 0
    for l in f:
        eqn = [int(i) for i in l.replace(":", "").split(" ")]
        if part1_helper(eqn, eqn[1]*eqn[2], 3) or part1_helper(eqn, eqn[1]+eqn[2], 3):
            res += eqn[0]

    return res

def part2_helper(eqn, curr_num, eqn_idx):
    if eqn_idx == len(eqn):
        if curr_num == eqn[0]:
            return True
        
        else:
            return False

    if curr_num > eqn[0]:
        return False
    
    return part2_helper(eqn, curr_num * eqn[eqn_idx], eqn_idx+1) or part2_helper(eqn, curr_num + eqn[eqn_idx], eqn_idx+1) or part2_helper(eqn, concat(curr_num, eqn[eqn_idx]), eqn_idx+1)
                

def part2(f):
    res = 0
    for l in f:
        eqn = [int(i) for i in l.replace(":", "").split(" ")]
        if part2_helper(eqn, eqn[1]*eqn[2], 3) or part2_helper(eqn, eqn[1]+eqn[2], 3) or part2_helper(eqn, concat(eqn[1], eqn[2]), 3):
            res += eqn[0]
    return res

