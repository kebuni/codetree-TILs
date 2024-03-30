import sys
from collections import deque
INT_MAX = sys.maxsize
q = deque()

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

N, M, K = map(int,input().split())

turret = []
recent_attack = [[0 for j in range(M)] for i in range(N)]
broken = [[False for j in range(M)] for i in range(N)]
involve_attack = [[False for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]
back_x = [[0 for j in range(M)] for i in range(N)]
back_y = [[0 for j in range(M)] for i in range(N)]

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if not elem:
            broken[x][y] = True
    turret.append(line)

######################################

def print_grid(grid):
    for x in range(N):
        for y in range(M):
            print(grid[x][y],end=' ')
        print()
    print()
    return

def select_attacker_and_victim():
    min_turret = (INT_MAX,INT_MAX,INT_MAX,INT_MAX)
    attacker = (100,100)
    max_turret = (-INT_MAX,-INT_MAX,-INT_MAX,-INT_MAX)
    victim = (100,100)
    for x in range(N):
        for y in range(M):
            if not broken[x][y]:
                temp = (turret[x][y],recent_attack[x][y],-(x+y),-y)
                if temp < min_turret:
                    min_turret = temp
                    attacker = (x,y)
                if temp > max_turret:
                    max_turret = temp
                    victim = (x,y)

    #print(attacker, victim)
    ax, ay = attacker
    turret[ax][ay] += (M+N)
    return attacker, victim

def attack(attacker,victim):
    global min_length, min_path, temp_path
    ax, ay = attacker
    vx, vy = victim

    clear_visited()
    clear_involve_attack()

    # dfs로 attack 부터 victim까지 경로 찾기
    can_attack = bfs(ax,ay,vx,vy)

    # 가능하면 레이저 공격
    if can_attack:
        laser_attack(ax,ay,vx,vy)
    # 불가능하면 포탄공격
    else:
        bomb_attack(ax,ay,vx,vy)

    update_recent_attack(attacker)
    return

def bfs(ax,ay,vx,vy):
    visited[ax][ay] = True
    q.clear()
    q.append((ax,ay))
    can_attack = False
    while q:
        x, y = q.popleft()
        # print("bfs:",x,y)

        if (x,y) == (vx,vy):
            can_attack = True
            break

        for dx, dy in zip(dxs,dys):
            nx, ny = (x + dx + N) % N, (y + dy + M) % M
            if can_go(nx,ny):
                push(x,y,nx,ny)

    # print("bfs done")
    return can_attack

def can_go(x,y):
    return not visited[x][y] and not broken[x][y]

def laser_attack(ax,ay,vx,vy):

    # print_grid(back_x)
    # print_grid(back_y)

    turret[vx][vy] -= turret[ax][ay]
    involve_attack[ax][ay] = True
    involve_attack[vx][vy] = True

    x = back_x[vx][vy]
    y = back_y[vx][vy]

    while (x,y) != (ax,ay):
        # print("x,y:",x,y)
        turret[x][y] -= turret[ax][ay] // 2
        involve_attack[x][y] = True

        next_x = back_x[x][y]
        next_y = back_y[x][y]
        x = next_x
        y = next_y

    return

def bomb_attack(ax,ay,vx,vy):
    dxs2 = [-1,-1,0,1,1,1,0,-1]
    dys2 = [0,1,1,1,0,-1,-1,-1]
    turret[vx][vy] -= turret[ax][ay]
    involve_attack[ax][ay] = True
    involve_attack[vx][vy] = True
    for dx, dy in zip(dxs2,dys2):
        nx, ny = (vx + dx + N) % N, (vy + dy + M) % M
        if not broken[nx][ny] and (nx,ny) != (ax,ay):
            turret[nx][ny] -= turret[ax][ay]//2
            involve_attack[nx][ny] = True

    return

def clear_visited():
    for x in range(N):
        for y in range(M):
            visited[x][y] = False
            back_x[x][y] = 0
            back_y[x][y] = 0
    return

def clear_involve_attack():
    for x in range(N):
        for y in range(M):
            involve_attack[x][y] = False
    return

def push(x,y,nx,ny):
    visited[nx][ny] = True
    back_x[nx][ny] = x
    back_y[nx][ny] = y
    q.append((nx,ny))
    return

def update_recent_attack(attacker):
    ax, ay = attacker
    for x in range(N):
        for y in range(M):
            recent_attack[x][y] += 1
    recent_attack[ax][ay] = 0
    return

def update_broken():
    for x in range(N):
        for y in range(M):
            if turret[x][y] <= 0:
                turret[x][y] = 0
                broken[x][y] = True
    return

def fix_turret():
    for x in range(N):
        for y in range(M):
            if not broken[x][y] and not involve_attack[x][y]:
                turret[x][y] += 1
    return

def check_end():
    result = 0
    for x in range(N):
        for y in range(M):
            if not broken[x][y]:
                result += 1
    return result <= 1

def print_max_power():
    print(max([turret[x][y] for x in range(N) for y in range(M)]))
    return

######################################

for _ in range(K):
    # print('---------------------')
    if check_end():
        # print('end')
        break
    attacker, victim = select_attacker_and_victim()
    # print("attacker:",attacker,"victim:",victim)

    attack(attacker,victim)
    # print("after attack")
    # print_grid(turret)
    # print_grid(recent_attack)
    # print_grid(involve_attack)

    update_broken()
    # print("after update broken")
    # print_grid(broken)

    fix_turret()
    # print_grid(turret)

print_max_power()