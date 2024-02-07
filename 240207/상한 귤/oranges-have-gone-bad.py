from collections import deque

grid = []
rotten_list = []
fresh_list = []
visited = []
step = []
q = deque()

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

################################
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y]==1

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()

def push(x,y,s):
    visited[x][y] = 1
    step[x][y] = s
    q.append((x,y))
    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return

################################
N, K = map(int,input().split())
for x in range(N):
    line = list(map(int,input().split()))
    grid.append(line)
    for y, elem in enumerate(line):
        if elem == 2:
            rotten_list.append((x,y))
        elif elem == 1:
            fresh_list.append((x,y))
    visited.append([0 for i in range(N)])
    step.append([-1 for i in range(N)])

for x,y in rotten_list:
    push(x,y,0)

bfs()

for x, y in fresh_list:
    if step[x][y] == -1:
        step[x][y] = -2

print_step()