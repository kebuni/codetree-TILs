import copy

N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
original_grid = copy.deepcopy(grid)
next_grid = [[0 for i in range(N)] for j in range(N)]
selected = []
final_ans = 0

################

def select(n):
    global grid, next_grid
    if n == 5:
        grid = copy.deepcopy(original_grid)
        simulate()
        find_max()
        return

    for i in range(4):
        selected.append(i)
        select(n+1)
        selected.pop()

    return

def simulate():

    for d in selected:
        clear_next_grid()
        check_double(d)
        move(d)
        copy_grid()
    return

def check_double(d):
    if d == 0: #상
        for col in range(N):
            prev = 0
            idx = -1
            for row in range(N):
                cur = grid[row][col]
                if cur: #만약 현재칸이 0이 아니라면?!
                    if cur == prev: #콤보가 됐다면!
                        grid[idx][col] = 0
                        grid[row][col] *= 2
                        prev = 0
                        idx = -1
                    else: #콤보가 안됐으면
                        prev = cur
                        idx = row
    elif d == 1: #우
        for row in range(N):
            prev = 0
            idx = -1
            for col in range(N-1,-1,-1):
                cur = grid[row][col]
                if cur: #만약 현재칸이 0이 아니라면?!
                    if cur == prev: #콤보가 됐다면!
                        grid[row][idx] = 0
                        grid[row][col] *= 2
                        prev = 0
                        idx = -1
                    else: #콤보가 안됐으면
                        prev = cur
                        idx = col
    elif d == 2: #하
        for col in range(N):
            prev = 0
            idx = -1
            for row in range(N-1,-1,-1):
                cur = grid[row][col]
                if cur: #만약 현재칸이 0이 아니라면?!
                    if cur == prev: #콤보가 됐다면!
                        grid[idx][col] = 0
                        grid[row][col] *= 2
                        prev = 0
                        idx = -1
                    else: #콤보가 안됐으면
                        prev = cur
                        idx = row
    else: #좌
        for row in range(N):
            prev = 0
            idx = -1
            for col in range(N):
                cur = grid[row][col]
                if cur: #만약 현재칸이 0이 아니라면?!
                    if cur == prev: #콤보가 됐다면!
                        grid[row][idx] = 0
                        grid[row][col] *= 2
                        prev = 0
                        idx = -1
                    else: #콤보가 안됐으면
                        prev = cur
                        idx = col

    return

def move(d):
    global next_grid
    if d == 0: #상
        for col in range(N):
            idx = 0
            for row in range(N):
                if grid[row][col]:
                    next_grid[idx][col] = grid[row][col]
                    idx += 1
    elif d == 1: #우
        for row in range(N):
            idx = N-1
            for col in range(N-1,-1,-1):
                if grid[row][col]:
                    next_grid[row][idx] = grid[row][col]
                    idx -= 1
    elif d == 2: #하
        for col in range(N):
            idx = N-1
            for row in range(N-1,-1,-1):
                if grid[row][col]:
                    next_grid[idx][col] = grid[row][col]
                    idx -= 1
    else: #좌
        for row in range(N):
            idx = 0
            for col in range(N):
                if grid[row][col]:
                    next_grid[row][idx] = grid[row][col]
                    idx += 1
    return

def copy_grid():
    global grid
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]
    return

def clear_next_grid():
    global next_grid
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = 0
    return

def find_max():
    global final_ans
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans,grid[i][j])
    final_ans = max(ans,final_ans)
    # if ans > final_ans:
    #     final_ans = max(ans, final_ans)
    #     print_grid()

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()
    print()

################

select(0)
print(final_ans)