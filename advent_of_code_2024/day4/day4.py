import os

def day4(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day4.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)
        

def check_dir(grid, i, j, x, y):
    XMAS = "XMAS"
    for c in XMAS:
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j] != c :
            return 0
        
        i += x
        j += y

    return 1

def check_mas(grid, i, j):
    if not 0<i<len(grid)-1 or not 0<j<len(grid[0])-1:
        return 0
    
    lr = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
    if not (lr == "MAS" or lr == "SAM"):
        return 0
    
    rl = grid[i+1][j-1] + grid[i][j] + grid[i-1][j+1]
    if not (rl == "MAS" or rl == "SAM"):
        return 0
    
    return 1

    

def part1(f):
    grid = [line.strip() for line in f]
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                res += check_dir(grid, i, j, -1, 0)
                res += check_dir(grid, i, j, 0, -1)
                res += check_dir(grid, i, j, -1, -1)
                res += check_dir(grid, i, j, 1, 1)
                res += check_dir(grid, i, j, 0, 1)
                res += check_dir(grid, i, j, 1, 0)
                res += check_dir(grid, i, j, -1, 1)
                res += check_dir(grid, i, j, 1, -1)
                
    return res
                


def part2(f):
    grid = [line.strip() for line in f]
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'A':
                res += check_mas(grid, i, j)

    return res