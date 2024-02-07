from collections import deque

grid = []
visited = []
step = []

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

q = deque()

####################

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y]

def push(x,y,s):
    global step, visited
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
        for j in range(M):
            print(step[i][j],end=' ')
        print()

####################

N, M = map(int,input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([0 for i in range(M)])
    step.append([0 for i in range(M)])

push(0,0,0)
bfs()
#print_step()

if step[N-1][M-1]==0:
    print(-1)
else:
    print(step[N-1][M-1])