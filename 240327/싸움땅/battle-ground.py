dxs = [-1,0,1,0]
dys = [0,1,0,-1]
d_to_arrow = ['↑','→','↓','←']

NO_PLAYER = (-1,-1,-1)

N, M, K = map(int,input().split())
gun_grid = [[[] for i in range(N)] for j in range(N)]
player_grid = [[NO_PLAYER for i in range(N)] for j in range(N)]
scores = [0 for i in range(M)]
init_stat = [0 for i in range(M)]
player_pos = [(-1,-1) for i in range(M)]

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem:
            gun_grid[x][y].append(elem)

for i in range(M):
    x, y, d, s = map(int,input().split())
    player_grid[x-1][y-1] = (i,d,0)
    player_pos[i] = (x-1,y-1)
    init_stat[i] = s

#######################################
def print_gun_grid():
    for x in range(N):
        for y in range(N):
            print(gun_grid[x][y],end=' ')
        print()
    print()
    return

def print_player_grid():
    for x in range(N):
        for y in range(N):
            if player_grid[x][y] == NO_PLAYER:
                print('(   )',end=' ')
            else:
                i, d, g = player_grid[x][y]
                print(f'({i}{d_to_arrow[d]}{g})',end=' ')
        print()
    print()
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N
def move_player(i):
    x, y = player_pos[i]
    pi, pd, pgun = player_grid[x][y]

    nx, ny = x + dxs[pd], y + dys[pd]
    if not in_range(nx,ny):
        pd = (pd + 2) % 4
    nx, ny = x + dxs[pd], y + dys[pd]

    if player_grid[nx][ny] == NO_PLAYER: # 이동한 곳에 플레이어가 없음

        player_grid[nx][ny] = (pi,pd,pgun)
        player_grid[x][y] = NO_PLAYER
        player_pos[pi] = (nx,ny)
        # 가장 좋은 총을 갖고, 갖고 있던 총은 내려 놓는다.
        get_best_gun(nx,ny)

    else:
        qi, qd, qgun = player_grid[nx][ny]
        player_grid[x][y] = NO_PLAYER
        player_grid[nx][ny] = NO_PLAYER
        battle(nx,ny,pi,pd,pgun,qi,qd,qgun)

    return

def battle(x,y,pi,pd,pgun,qi,qd,qgun):
    p_power = (init_stat[pi] + pgun, init_stat[pi])
    q_power = (init_stat[qi] + qgun, init_stat[qi])
    if p_power > q_power:
        scores[pi] += p_power[0] - q_power[0]
        lose(x,y,qi,qd,qgun)
        win(x,y,pi,pd,pgun)
    else:
        scores[qi] += q_power[0] - p_power[0]
        lose(x,y,pi,pd,pgun)
        win(x,y,qi,qd,qgun)
    return

def lose(x,y,idx,d,gun):
    # x,y에 총을 내려 놓고
    if gun:
        gun_grid[x][y].append(gun)
    # 새로운 위치를 찾고 이동, 위치 업데이트
    nx, ny = 100, 100
    for i in range(4):
        nd = (d + i) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        if in_range(nx,ny) and player_grid[nx][ny] == NO_PLAYER:
            player_grid[nx][ny] = (idx,nd,0)
            player_pos[idx] = (nx,ny)
            break
    # 총 줍기
    get_best_gun(nx,ny)
    return

def win(x,y,i,d,gun):
    # 위치 업데이트
    player_grid[x][y] = (i,d,gun)
    player_pos[i] = (x,y)
    # 총 줍기
    get_best_gun(x,y)
    return

def find_possible_pos(x,y,d):
    for i in range(4):
        nd = (d + i) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        if in_range(nx,ny) and player_grid[nx][ny] == NO_PLAYER:
            return nx, ny, nd
    return 100,100,100

def get_best_gun(x,y):
    if not gun_grid[x][y]:
        return

    idx, d, my_gun = player_grid[x][y]
    guns = gun_grid[x][y]
    best_gun = max(guns)

    # 땅에 있던 총이 더 좋다면?
    if my_gun < best_gun:
        guns.remove(best_gun)
        if my_gun:
            guns.append(my_gun)
        player_grid[x][y] = (idx,d,best_gun)

    return

#######################################

for _ in range(K):
    for i in range(M):
        move_player(i)
        # print("after move",i)
        # print_player_grid()
        # print_gun_grid()
        # print(player_pos)
        # print(scores)

for i in range(M):
    print(scores[i],end=' ')