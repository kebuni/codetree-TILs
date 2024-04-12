import sys
from collections import deque
OUT_OF_INDEX = 1000
OUT_OF_GRID = (OUT_OF_INDEX, OUT_OF_INDEX)
INT_MAX = sys.maxsize

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

N, M, K = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
last = [[0 for i in range(M)] for j in range(N)]
prev = [[OUT_OF_GRID for i in range(M)] for j in range(N)]
visited = [[False for i in range(M)] for j in range(N)]

q = deque()
involved = set()

#######################################################

def select_attacker():
    best = (INT_MAX, INT_MAX, INT_MAX, INT_MAX)
    best_x, best_y = OUT_OF_GRID

    for x in range(N):
        for y in range(M):
            # 부서지지 않았다면
            if grid[x][y] > 0:
                temp = (grid[x][y], last[x][y], -(x+y), -y)
                if temp < best:
                    best = temp
                    best_x, best_y = x, y

    grid[best_x][best_y] += (M+N)

    # 잘못된 리턴 가능성? : check_end로 인해 무조건 둘 이상 포탑이 살아있음
    return best_x, best_y

def select_victim(ax,ay):
    best = (-INT_MAX, -INT_MAX, -INT_MAX, -INT_MAX)
    best_x, best_y = OUT_OF_GRID

    for x in range(N):
        for y in range(M):
            # 부서지지 않았고, 공격자가 아니라면
            if grid[x][y] > 0 and (x,y) != (ax,ay):
                temp = (grid[x][y], last[x][y], -(x+y), -y)
                if temp > best:
                    best = temp
                    best_x, best_y = x, y

    return best_x, best_y

def bfs(ax,ay,vx,vy):
    q.clear()
    clear_visited_and_prev()
    push(ax,ay)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = (x + dx + N) % N, (y + dy + M) % M
            if can_go(nx,ny):
                prev[nx][ny] = (x,y)
                push(nx,ny)

    # vx, vy에 도달이 가능한지 여부를 리턴하여 알맞는 공격을 합니다.
    return visited[vx][vy]

def can_go(x,y):
    return not visited[x][y] and grid[x][y] > 0

def push(x,y):
    visited[x][y] = True
    q.append((x,y))
    return

def clear_visited_and_prev():
    for x in range(N):
        for y in range(M):
            visited[x][y] = False
            prev[x][y] = OUT_OF_GRID
    return

def laser_attack(ax,ay,vx,vy):
    # involved도 업데이트 해줘야 합니다.

    involved.add((ax, ay))
    involved.add((vx, vy))
    grid[vx][vy] -= grid[ax][ay]

    x, y = prev[vx][vy]
    while (x,y) != (ax,ay):
        grid[x][y] -= grid[ax][ay] // 2
        involved.add((x,y))
        x, y = prev[x][y]

    return

def bomb_attack(ax,ay,vx,vy):
    # involved도 업데이트 해줘야 합니다.
    dxs2 = [0,1,1,1,0,-1,-1,-1]
    dys2 = [1,1,0,-1,-1,-1,0,1]

    involved.add((ax,ay))

    grid[vx][vy] -= grid[ax][ay]
    involved.add((vx,vy))
    for dx, dy in zip(dxs2, dys2):
        nx, ny = (vx + dx + N) % N, (vy + dy + M) % M
        # TODO : 피해입을 때 0 이어도 상관없는건가
        if (nx, ny) != (ax, ay):
            grid[nx][ny] -= grid[ax][ay] // 2
            involved.add((nx,ny))

    return

def update_last(ax,ay):
    for x in range(N):
        for y in range(M):
            if (x,y) == (ax,ay):
                last[x][y] = 0
            else:
                last[x][y] += 1
    return

def update_turret():
    for x in range(N):
        for y in range(M):
            if grid[x][y] < 0:
                grid[x][y] = 0
    return

def fix_turret():
    # 부서지지 않고 공격과 무관하면 1씩 증가
    for x in range(N):
        for y in range(M):
            if grid[x][y] > 0:
                if (x,y) not in involved:
                    grid[x][y] += 1

    # 공격 관련 set 초기화
    involved.clear()
    return

def check_end():
    remain = 0
    for x in range(N):
        for y in range(M):
            if grid[x][y] > 0:
                remain += 1
    return remain <= 1

def print_ans():
    print(max([grid[x][y] for x in range(N) for y in range(M)]))
    return

def print_grid(A):
    for x in range(N):
        for y in range(M):
            print(A[x][y],end=' ')
        print()
    print()
    return

#######################################################

for i in range(K):

    # print("======================",i)

    ax, ay = select_attacker()
    # print("after select attacker:",ax,ay)

    vx, vy = select_victim(ax,ay)
    # print("after select victim:", vx, vy)

    laser = bfs(ax,ay,vx,vy)
    # print("after bfs")
    # print_grid(prev)

    if laser:
        # print("laser")
        laser_attack(ax,ay,vx,vy)
    else:
        # print("bomb")
        bomb_attack(ax,ay,vx,vy)

    # print("after attack:")
    # print_grid(grid)
    # print("involved:",involved)

    update_last(ax,ay)
    # print("after update last")
    # print_grid(last)

    update_turret()
    # print("after update turret")
    # print_grid(grid)

    fix_turret()
    # print("after fix turret")
    # print("involved:",involved)
    # print_grid(grid)

    if check_end():
        # print("check end")
        break

print_ans()