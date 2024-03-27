dxs = [-1,0,1,0]
dys = [0,1,0,-1]
d_to_arrow = ['↑','→','↓','←']

N, M, K = map(int,input().split())
gun_grid = [[[] for i in range(N)] for j in range(N)]
player_grid = [[[] for i in range(N)] for j in range(N)]
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
    player_grid[x-1][y-1].append((i,d,0))
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

            print('[',end='')
            for i, d, g in player_grid[x][y]:
                print('(',end='')
                print(i,d_to_arrow[d],g,end='')
                print(')',end='')
            print(']',end=' ')
        print()
    print()
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N
def move_player(i):
    x, y = player_pos[i]
    pi, pd, pgun = player_grid[x][y][0]

    nx, ny = x + dxs[pd], y + dys[pd]
    if not in_range(nx,ny):
        pd = (pd + 2) % 4
    nx, ny = x + dxs[pd], y + dys[pd]

    if not player_grid[nx][ny]: # 이동한 곳에 플레이어가 없음
        update_pos(pi,pd,pgun,x,y,nx,ny)
        # 가장 좋은 총을 갖고, 갖고 있던 총은 내려 놓는다.
        get_best_gun(nx,ny)
    else: # 이동한 곳에 다른 플레이어가 있음
        qi, qd, qgun = player_grid[nx][ny][0]
        p_power = (init_stat[pi]+pgun, init_stat[pi])
        q_power = (init_stat[qi]+qgun, init_stat[qi])
        if p_power > q_power: # p가 이긴 경우
            diff = p_power[0] - q_power[0]
            scores[pi] += diff

            # q 총 내려놓기
            if qgun:
                gun_grid[nx][ny].append(qgun)
            # p 빼기
            player_grid[x][y].pop()
            # q 가능한 위치 찾기
            qnx, qny, nqd = find_possible_pos(nx,ny,qd)
            # q 위치 옮기고 pos 업데이트
            update_pos(qi,nqd,0,nx,ny,qnx,qny)
            # q 총줍기
            get_best_gun(qnx,qny)
            # p 넣기
            player_grid[x][y].append((pi,pd,pgun))
            # p 위치 nx,ny로 업데이트
            update_pos(pi,pd,pgun,x,y,nx,ny)
            # p 총줍기
            get_best_gun(nx,ny)

        else: # q가 이긴 경우
            diff = q_power[0] - p_power[0]
            scores[qi] += diff

            # p 총 내려놓기
            if pgun:
                gun_grid[nx][ny].append(pgun)
            # p 새로운 위치찾기
            pnx, pny, pnd = find_possible_pos(nx,ny,pd)
            # p 위치 옮기고 pos 업데이트
            update_pos(pi,pnd,0,x,y,pnx,pny)
            # p 총줍기
            get_best_gun(pnx,pny)
            # q 총줍기
            get_best_gun(nx,ny)

    return

def update_pos(idx,d,gun,x,y,nx,ny):
    player_grid[nx][ny].append((idx,d,gun))
    player_grid[x][y].pop()
    player_pos[idx] = (nx,ny)
    return

def find_possible_pos(x,y,d):
    for i in range(4):
        nd = (d + i) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        if in_range(nx,ny) and not player_grid[nx][ny]:
            return nx, ny, nd
    return 100,100,100

def get_best_gun(x,y):
    if not gun_grid[x][y]:
        return

    idx, d, my_gun = player_grid[x][y][0]
    guns = gun_grid[x][y]
    best_gun = max(guns)

    # 땅에 있던 총이 더 좋다면?
    if my_gun < best_gun:
        guns.remove(best_gun)
        if my_gun:
            guns.append(my_gun)
        player_grid[x][y].pop()
        player_grid[x][y].append((idx,d,best_gun))

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