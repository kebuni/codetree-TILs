from collections import deque
import sys

original_grid = []
grid = []
visited = []
step = []
ans = sys.maxsize

wall_list = []
selected = []
q = deque()

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

##############################

def choose(n,cnt):
    global ans

    if n == len(wall_list):
        if cnt == K:
            clear_step_and_visited()
            copy_grid()
            remove_wall()

            push(start_x,start_y,0)
            bfs()

            #print_step()
            #print(step[end_x][end_y])
            #print()

            if step[end_x][end_y] != -1:
                ans = min(ans,step[end_x][end_y])

        return
    
    selected.append(wall_list[n])
    choose(n+1,cnt+1)
    selected.pop()
    choose(n+1,cnt)

    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == 0

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

def clear_step_and_visited():
    for i in range(N):
        for j in range(N):
            step[i][j] = -1
            visited[i][j] = 0
    return

def copy_grid():
    for i in range(N):
        for j in range(N):
            grid[i][j] = original_grid[i][j]
    return

def remove_wall():
    for x, y in selected:
        grid[x][y] = 0
    return

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    # print()

##############################

N, K = map(int,input().split())
for x in range(N):
    line = list(map(int,input().split()))
    original_grid.append(line.copy())
    grid.append(line.copy())
    for y, elem in enumerate(line):
        if elem == 1:
            wall_list.append((x,y))
    visited.append([0 for i in range(N)])
    step.append([-1 for i in range(N)])

start_x, start_y = map(int,input().split())
start_x -= 1
start_y -= 1
end_x, end_y = map(int,input().split())
end_x -= 1
end_y -= 1

choose(0,0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)