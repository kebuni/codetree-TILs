from collections import deque

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
cur_size = 0

q = deque()
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
ans = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,s):
    return in_range(x,y) and s > 0 and not visited[x][y]

def clear_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

def push(x,y,s):
    global cur_size
    cur_size += 1
    visited[x][y] = True
    q.append((x,y,s))
    return

def bfs():
    while q:
        x, y, s = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny, ns = x + dx, y + dy, s - 1
            if can_go(nx,ny,ns):
                push(nx,ny,ns)
    return

def get_gold():
    sum = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                sum += grid[i][j]
    return sum

def get_cost(s):
    return s*s + ((s+1) * (s+1))

def print_visited():
    for i in range(N):
        for j in range(N):
            print(visited[i][j],end=' ')
        print()
    print()

for x in range(N):
    for y in range(N):
        for s in range(1,N+1):
            cur_size = 0
            clear_visited()
            push(x,y,s)
            bfs()
            #print_visited()
            #print(get_gold(),get_gold()*M,get_cost(s-1))
            if get_gold()*M >= get_cost(s-1):
                #print("yeah!!")
                ans = max(ans,get_gold())

print(ans)