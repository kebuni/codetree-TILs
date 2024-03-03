from collections import deque
OUT_OF_GRID = 100,100

N = int(input())

dxs = [-1,0,1,0]
dys = [0,-1,0,1]

rx, ry = 0,0
level = 2
cur_kill = 0

grid = []
step = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
q = deque()

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem == 9:
            rx, ry = x, y
    grid.append(line)

grid[rx][ry] = 0
ans = 0

####################################

def find_enemy():
    return

def go_battle(ex,ey):
    return

def clear_step():
    for i in range(N):
        for j in range(N):
            step[i][j] = 0
            visited[i][j] = False

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))
    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] <= level

def find_enemy():
    ex, ey = OUT_OF_GRID
    min_dist = 987654321
    for x in range(N):
        for y in range(N):
            # 만약 자신의 레벨보다 낮은 적이 있는 칸이라면,
            if step[x][y] and 0 < grid[x][y] < level:
                # 더 가까이 있는 적이라면
                if step[x][y] < min_dist:
                    min_dist = step[x][y]
                    ex, ey = x, y
    return ex, ey

def go_battle(ex,ey):
    # 로봇이 x,y에 있는 적을 잡습니다
    # 적의 위치를 0으로 바꾸고 ans를 더해줍니다
    # 만약 로봇이 자기 레벨만큼 잡으면 레벨을 올리고 잡은 수를 초기화 합니다

    global rx, ry, ans, cur_kill, level
    rx, ry = ex, ey
    grid[rx][ry] = 0
    ans += step[rx][ry]
    cur_kill += 1

    if cur_kill == level:
        cur_kill = 0
        level += 1

    return

def print_grids():
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end= ' ')
        print('\t\t',end=' ')
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    print()

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    print()

####################################



while True:

    clear_step()
    push(rx,ry,0)
    bfs()
    #print("after bfs: ")
    #print_step()

    ex, ey = find_enemy()
    #print("next enemy:", ex, ey)

    if (ex, ey) != OUT_OF_GRID:
        go_battle(ex,ey)
    else:
        break

    #print(rx, ry, level, cur_kill, ans)
    #print_grids()

print(ans)