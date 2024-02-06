from collections import deque

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

grid = []
visited = []
starts = []
q = deque()
sum = 0
#########################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y]:
        return False
    return True

def push(x,y):
    global visited, sum, q
    visited[x][y] = True
    sum += 1
    q.append((x,y))
    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny)

    return


#########################

N, K = map(int,input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([False for i in range(N)])

for _ in range(K):
    r, c = map(int,input().split())
    starts.append((r-1,c-1))

for x, y in starts:
    if not visited[x][y]:
        push(x,y)
        bfs()

print(sum)