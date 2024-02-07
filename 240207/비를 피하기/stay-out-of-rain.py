from collections import deque
import sys

INT_MAX = sys.maxsize

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
grid = []
step = []
visited = []
ans_grid = []
safe_list = []
human_list = []
q = deque()

#################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] != 1

def push(x,y,s):
    visited[x][y] = 1
    step[x][y] = s
    q.append((x,y))
    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    print()

def print_ans_grid():
    for i in range(N):
        for j in range(N):
            print(ans_grid[i][j],end=' ')
        print()

def clear_step_and_visited():
    for i in range(N):
        for j in range(N):
            step[i][j] = -1
            visited[i][j] = 0
    return

def update_ans_grid():
    global ans_grid
    for x,y in human_list:
        if step[x][y] != -1:
            ans_grid[x][y] = min(ans_grid[x][y],step[x][y])
    return

################################

N, H, M = map(int,input().split())
for x in range(N):
    line = list(map(int,input().split()))
    grid.append(line)
    for y, elem in enumerate(line):
        if elem == 3:
            safe_list.append((x,y))
        elif elem == 2:
            human_list.append((x,y))
    step.append([-1 for i in range(N)])
    visited.append([0 for i in range(N)])
    ans_grid.append([0 for i in range(N)])

for x, y in human_list:
    ans_grid[x][y] = INT_MAX

# for x, y in safe_list:
#     clear_step_and_visited()
#     push(x,y,0)
#     bfs()
#     update_ans_grid()

#     print_step()

for x, y in safe_list:
    push(x,y,0)

bfs()

for x, y in human_list:
    ans_grid[x][y] = step[x][y]

# for x, y in human_list:
#     if ans_grid[x][y] == INT_MAX:
#         ans_grid[x][y] = -1

print_ans_grid()