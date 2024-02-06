from collections import deque

grid = []
visited = []
start_num = -1
q = deque()
destination = [-1,-1,-1]

dxs = [-1,0,1,0]
dys = [0,-1,0,1]

#############################
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] >= start_num:
        return False
    return True

def is_better(num,x,y):
    if num > destination[0]:
        return True
    elif num == destination[0]:
        return (x,y) < (destination[1],destination[2])
    else:
        return False

def clear_visited():
    global visited
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

def push(x,y):
    #print("push",x,y)
    global visited, q, destination
    visited[x][y] = True
    if is_better(grid[x][y],x,y):
        destination = [grid[x][y],x,y]
        #print("here",destination)
    q.append((x,y))
    return

def bfs():
    global q,visited
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny)
    return

###########################

N, K = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([False for i in range(N)])

r,c = map(int,input().split())

destination[0] = grid[r-1][c-1]
destination[1] = r-1
destination[2] = c-1
for _ in range(K):
    clear_visited()
    start_num = destination[0]
    destination[0] = -1
    visited[destination[1]][destination[2]] = True
    q.append((destination[1],destination[2]))
    bfs()
    #print(destination)

print(destination[1]+1,destination[2]+1)