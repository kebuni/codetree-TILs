from collections import deque

N, M = map(int,input().split())
map_grid = [list(map(int,input().split())) for i in range(N)]
dest = [(-1,-1)]
for i in range(M):
    x, y = map(int,input().split())
    dest.append((x-1,y-1))

grid = [[[] for i in range(N)] for j in range(N)]
next_grid = [[[] for i in range(N)] for j in range(N)]
step = [[-1 for i in range(N)] for j in range(N)]

arrival = [False for i in range(M+1)]
can_go_grid = [[True for i in range(N)] for j in range(N)]

dxs = [-1,0,0,1]
dys = [0,-1,1,0]
q = deque()

#####################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and step[x][y] == -1 and can_go_grid[x][y]

def move_all():
    for x in range(N):
        for y in range(N):
            for p in grid[x][y]:
                # 아직 도착하지 못한 사람이라면
                if not arrival[p]:
                    move_one(p,x,y)

    copy_and_clear_next_grid()
    return

def copy_and_clear_next_grid():
    for x in range(N):
        for y in range(N):
            grid[x][y] = next_grid[x][y][:]
            next_grid[x][y].clear()
    return

def move_one(p,x,y):
    # x,y 에 있는 p를 한칸 이동시킵니다.

    # p가 가고자 하는 목적지를 보고
    cx, cy = dest[p]
    # bfs를 해줍니다.
    bfs(cx,cy)

    # 상좌우하 순서로 가까워지는 곳으로 이동합니다
    nx, ny, min_dist = 100000, 100000, 100000
    for dx, dy in zip(dxs,dys):
        tx, ty = x + dx, y + dy
        if in_range(tx,ty) and step[tx][ty] != -1:
            dist = step[tx][ty]
            if dist < min_dist:
                nx, ny = tx, ty
                min_dist = dist

    next_grid[nx][ny].append(p)
    return

def bfs(x,y):
    clear_step()
    push(x,y,0)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y] + 1)
    return

def push(x,y,s):
    step[x][y] = s
    q.append((x,y))
    return

def clear_step():
    for x in range(N):
        for y in range(N):
            step[x][y] = -1
    return

def check_end():
    for i in range(1,M+1):
        if not arrival[i]:
            return False
    return True

def update_arrival():
    for x in range(N):
        for y in range(N):
            for p in grid[x][y]:
                if dest[p] == (x,y):
                    arrival[p] = True
                    can_go_grid[x][y] = False
    return

def set_basecamp(T):
    # T를 가고자 하는 편의점과 가장 가까운 유효한 베이스캠프에 세팅합니다.
    cx, cy = dest[T]
    bfs(cx,cy)

    bx, by, min_dist = 100000, 100000, 100000

    for x in range(N):
        for y in range(N):
            # 어떤 베이스캠프가
            if map_grid[x][y]:
                # 갈 수 있는 곳인데
                if step[x][y] != -1:
                    # 가장 가까운 곳이라면?
                    if step[x][y] < min_dist:
                        bx, by = x, y
                        min_dist = step[x][y]

    grid[bx][by].append(T)
    can_go_grid[bx][by] = False
    return

def print_grid():
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()

def print_can_go_grid():
    for x in range(N):
        for y in range(N):
            print(can_go_grid[x][y],end=' ')
        print()
    print()

#####################################

T = 1
while True:
    # print(T,'------------------')

    move_all()
    # print("after move all")
    # print_grid()
    # print_can_go_grid()

    update_arrival()
    # print("after update_arrival")
    # print(arrival)

    if T<= M:
        set_basecamp(T)
        # print("after set",T)
        # print_grid()
        # print_can_go_grid()

    if check_end():
        break

    T += 1

print(T)