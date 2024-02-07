from collections import deque
grid = []
visited = []
selected_start = []
q = deque()
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
cur_dist = 0
ans = 0

##############################

def choose_city(n,cnt):
    global ans, cur_dist
    if n==N*N:
        if cnt == K:
            clear_visited()
            cur_dist = 0
            #print(selected_start)
            for elem in selected_start:
                #print(elem//N, elem%N)
                x = elem // N
                y = elem % N
                if not visited[x][y]:
                    push(x,y)
                    bfs()
            #모든 도시에 대해 탐색이 끝났다면
            ans = max(ans,cur_dist)
            #print(ans)
        return
    
    
    selected_start.append(n)
    choose_city(n+1,cnt+1)
    selected_start.pop()

    choose_city(n+1,cnt)

    return

def push(x,y):
    global cur_dist, visited, q
    visited[x][y] = 1
    cur_dist += 1
    q.append((x,y))
    return

def bfs():
    global q
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            #print(x,y,nx,ny)
            if can_go(x,y,nx,ny):
                #print("can go!")
                push(nx,ny)
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,nx,ny):
    return in_range(nx,ny) and not visited[nx][ny] \
    and U <= abs(grid[nx][ny] - grid[x][y]) <= D

def clear_visited():
    global visited
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

##############################

N, K, U, D = map(int, input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([0 for i in range(N)])

choose_city(0,0)

print(ans)