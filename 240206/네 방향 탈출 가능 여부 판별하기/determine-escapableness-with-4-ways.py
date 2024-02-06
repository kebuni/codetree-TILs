from collections import deque

grid = []
visited = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()
########################
def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True

def push(x,y):
    global q, visited
    visited[x][y]=True
    q.append((x,y))
    return

def bfs():
    global q
    while q:
        x, y = q.popleft()
        #print(x,y)
        #print_grid()
       
        for dx, dy in zip(dxs,dys):
           nx = x + dx
           ny = y + dy
           if can_go(nx,ny):
               push(nx,ny)

    return

def print_grid():
    for i in range(N):
        for j in range(M):
            print(visited[i][j],end=' ')
        print()

########################

N, M = map(int,input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([False for i in range(M)])

push(0,0)
bfs()

if visited[N-1][M-1]:
    print(1)
else:
    print(0)