import sys
from collections import deque

N, M = map(int,input().split())

grid = []
hospitals = []
selected = []

visited = [[False for i in range(N)] for j in range(N)]
step = [[-1 for i in range(N)] for j in range(N)]
q = deque()

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

ans = sys.maxsize

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem == 2:
            hospitals.append((x,y))
    grid.append(line)

#############################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] != 1

def choose_hospital(n,m):
    global ans
    if m == M:
        # 선택된 병원을 push하고 bfs한뒤 check, ans 업데이트
        clear_grids()
        for x, y in selected:
            push(x,y,0)
        bfs()
        #print_step()
        if check_all_virus_dead():
            ans = min(ans, max_time())
        return

    if n == len(hospitals):
        return

    selected.append(hospitals[n])
    choose_hospital(n+1, m+1)
    selected.pop()
    choose_hospital(n+1, m)

    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y] + 1)
    return

def push(x,y,s):
    global q
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))
    return

def check_all_virus_dead():
    for i in range(N):
        for j in range(N):
            # 만약 bfs가 끝나도 가지 못한 곳인데 바이러스가 있는 곳이라면?
            if step[i][j] == -1 and grid[i][j] == 0:
                return False
    return True

def clear_grids():
    for i in range(N):
        for j in range(N):
            step[i][j] = -1
            visited[i][j] = False
    return

def max_time():
    t = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                t = max(t,step[i][j])
    return t

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    print()

#############################################

choose_hospital(0,0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)