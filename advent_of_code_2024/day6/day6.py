import os

from copy import deepcopy

def day6(part: int):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "day6.txt")
    with open(file_path, "r") as f:
        if part == 1:
            return part1(f)
        
        else:
            return part2(f)

def walk(grid, i, j, dx, dy):
    cnt = 0
    cont = True
    while True:
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
            cont = False
            break

        if grid[i][j] == '#':
            i -= dx
            j -= dy
            break

        if grid[i][j] == '.':
            grid[i][j] = 'x'
            cnt += 1
        
        i += dx
        j += dy

    
    return cnt, cont, i, j

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

def part1(f):
    res = 1
    grid = [list(line.strip()) for line in f]
    x = 0
    y = 0
    for i, a in enumerate(grid):
        if '^' in a:
            y = a.index('^')
            x = i
            break

    dir_idx = 0
    cont = True    
    while cont:
        cnt, cont, x, y = walk(grid, x, y, DIRS[dir_idx][0], DIRS[dir_idx][1])
        dir_idx = (dir_idx+1)%4
        res += cnt


    return res
                

def part2(f):
    res = 0
    grid = [list(line.strip()) for line in f]
    initial_x = 0
    initial_y = 0
    for i, a in enumerate(grid):
        if '^' in a:
            initial_y = a.index('^')
            initial_x = i
            break

    start_and_end_coords = set()
    for block_i, a in enumerate(grid):
        for block_j, _ in enumerate(a):
            x_start = initial_x
            y_start = initial_y
            dir_idx = 0
            if grid[block_i][block_j] == '#':
                continue
            
            grid[block_i][block_j] = '#'
            cont = True
            while cont:
                _, cont, new_x, new_y = walk(grid, x_start, y_start, DIRS[dir_idx][0], DIRS[dir_idx][1])
                dir_idx = (dir_idx+1)%4
                if (x_start, y_start, new_x, new_y) in start_and_end_coords:
                    res += 1
                    break

                start_and_end_coords.add((x_start, y_start, new_x, new_y))
                x_start = new_x
                y_start = new_y
            
            start_and_end_coords.clear()
            grid[block_i][block_j] = '.'



    return res

