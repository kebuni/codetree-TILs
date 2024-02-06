from collections import deque
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
grid = []
removed_grid = []
visited = []
rocks = []
selected = []
starts = []
count = 0
ans = -1
q = deque()

############################

def choose(n,cnt):
    if n == len(rocks):
        if cnt == M:
            #print("all chosen", selected)
            remove_rock()
            start_bfs()
        return

    choose(n+1,cnt)
    selected.append(rocks[n])
    choose(n+1,cnt+1)
    selected.pop()

    return

def remove_rock():
    global removed_grid
    for i in range(N):
        for j in range(N):
            removed_grid[i][j] = grid[i][j]

    for x,y in selected:
        removed_grid[x][y] = 0

    #print_grid()
    #print_removed_grid()

    return

def start_bfs():
    global count,ans
    count = 0
    clear_visited()
    for x,y in starts:
        if not visited[x][y]:
            push(x,y)
            bfs()

    if count > ans:
        #print("new score!")
        #print(selected)
        #print("count ",count)
        ans = count
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if removed_grid[x][y]:
        return False
    return True

def bfs():
    global count, visited, q
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny)
    return

def push(x,y):
    global visited, q, count
    count += 1
    visited[x][y] = 1
    q.append((x,y))

def clear_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def print_removed_grid():
    for i in range(N):
        for j in range(N):
            print(removed_grid[i][j],end=' ')
        print()
############################

N, K, M = map(int,input().split())

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem:
            rocks.append((x,y))
    grid.append(line)
    removed_grid.append(line.copy())
    visited.append([0 for i in range(N)])

for _ in range(K):
    r, c = map(int,input().split())
    starts.append((r-1,c-1))

#print_grid()
#print('------------------')

choose(0,0)

print(ans)