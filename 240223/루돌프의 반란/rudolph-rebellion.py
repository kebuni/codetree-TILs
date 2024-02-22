INF = 987654321
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

DEBUG = False

N, M, P, C, D = map(int,input().split())

grid = [[0 for i in range(N)] for j in range(N)]
santa_score = [0 for i in range(P+1)]
santa_loc = [(INF,INF) for i in range(P+1)]
santa_stun = [0 for i in range(P+1)]
santa_alive = [True for i in range(P+1)]

rudol_x, rudol_y = map(int,input().split())
rudol_x -= 1; rudol_y -= 1
grid[rudol_x][rudol_y] = -1

for i in range(P):
    idx, x, y = map(int,input().split())
    santa_loc[idx] = (x-1,y-1)
    grid[x-1][y-1] = idx


###################################################
def print_grid():
    if DEBUG:
        for i in range(N):
            for j in range(N):
                print(grid[i][j],end=' ')
            print()
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def cal_dist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def move_rudolph():
    global rudol_x, rudol_y
    d = get_new_rudolph()
    grid[rudol_x][rudol_y] = 0
    rudol_x += dxs[d]
    rudol_y += dys[d]
    if grid[rudol_x][rudol_y] > 0:
        santa = grid[rudol_x][rudol_y]
        rudolph_crash(santa,rudol_x,rudol_y,d)
    grid[rudol_x][rudol_y] = -1
    return

def get_new_rudolph():
    nearest_santa = (INF, 0, 0)

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0:
                temp_santa = (
                cal_dist(rudol_x, rudol_y, i, j), -i, -j)
                if temp_santa < nearest_santa:
                    nearest_santa = temp_santa

    santa_x, santa_y = -nearest_santa[1], -nearest_santa[2]
    min_dist = INF
    min_d = 0
    for d in range(8):
        nx,ny = rudol_x + dxs[d], rudol_y + dys[d]
        temp_dist = cal_dist(santa_x,santa_y,nx,ny)
        if min_dist > temp_dist:
            min_dist = temp_dist
            min_d = d

    return min_d

def get_new_santa(i):
    x, y = santa_loc[i]
    min_direct = -1
    min_dist = cal_dist(x,y,rudol_x,rudol_y)
    for d in [0,2,4,6]:
        nx = x + dxs[d]
        ny = y + dys[d]
        if can_go(nx,ny):
            temp_dist = cal_dist(nx,ny,rudol_x,rudol_y)
            if temp_dist < min_dist:
                min_dist = temp_dist
                min_direct = d
    return min_direct

def rudolph_crash(i,x,y,d):
    # 산타 점수 추가
    santa_score[i] += C
    # 산타 위치 이동
    nx = x + C * dxs[d]
    ny = y + C * dys[d]
    # 산타 스턴
    santa_stun[i] = 2

    if in_range(nx,ny):
        # 산타 안나갔으면 인터랙션 & 그리드 표시
        interaction(i,nx,ny,d)
    else:
        # 산타 나가면 죽음 처리
        santa_loc[i] = (INF,INF)
        santa_alive[i] = False

    return

def santa_crash(i,x,y,d):
    # 산타 점수 추가
    santa_score[i] += D
    # 산타 위치 이동
    nx = x + D * dxs[d]
    ny = y + D * dys[d]
    # 산타 스턴
    santa_stun[i] = 2

    if in_range(nx, ny):
        # 산타 안나갔으면 인터랙션 & 그리드 표시
        interaction(i, nx, ny, d)
    else:
        # 산타 나가면 죽음 처리
        santa_loc[i] = (INF, INF)
        santa_alive[i] = False
    return

def interaction(i,start_x,start_y,d):

    last_x, last_y = start_x, start_y
    while in_range(last_x,last_y) and grid[last_x][last_y] > 0: #다른 산타가 있고 범위 안 이라면
        last_x += dxs[d]
        last_y += dys[d]

    # if not in_range(last_x, last_y):
    #     santa_alive[grid[last_x-dxs[d]][last_y-dys[d]]] = False
    #     santa_loc[grid[last_x-dxs[d]][last_y-dys[d]]] = (INF, INF)
    #     grid[last_x - dxs[d]][last_y - dys[d]] = 0
    #
    # cur_x, cur_y = last_x, last_y
    #
    # while cur_x != start_x or cur_y != start_y:
    #     before_x, before_y = cur_x - dxs[d], cur_y - dys[d]
    #     before_i = grid[before_x][before_y]
    #     grid[cur_x][cur_y] = grid[before_x][before_y]
    #     santa_loc[before_i] = (cur_x, cur_y)
    #     cur_x = before_x
    #     cur_y = before_y

    cur_x, cur_y = last_x, last_y
    while cur_x != start_x or cur_y != start_y:
        before_x, before_y = cur_x - dxs[d], cur_y - dys[d]

        if not in_range(before_x,before_y):
            break

        before_i = grid[before_x][before_y]

        if not in_range(cur_x,cur_y):
            santa_alive[before_i] = False
        else:
            grid[cur_x][cur_y] = grid[before_x][before_y]
            santa_loc[before_i] = (cur_x, cur_y)

        cur_x = before_x
        cur_y = before_y

    grid[start_x][start_y] = i
    santa_loc[i] = (start_x,start_y)
    return

def move_santas():

    for i in range(1,P+1):
        if santa_alive[i] and santa_stun[i] == 0: # 산타가 움직일 수 있으면
            x, y = santa_loc[i]
            d = get_new_santa(i)
            if d == -1:
                continue
            nx = x + dxs[d]
            ny = y + dys[d]
            grid[x][y] = 0

            if nx == rudol_x and ny == rudol_y:
                log_name("crash!!!")
                santa_crash(i,nx,ny,(d+4)%8)
            else:
                grid[nx][ny] = i
                santa_loc[i] = (nx,ny)

    return

def wake_santas():
    for i in range(1,P+1):
        if santa_stun[i] > 0:
            santa_stun[i] -= 1
    return

def is_ended():
    for i in range(1,P+1):
        if santa_alive[i]:
            return False
    return True

def get_point():
    for i in range(1,P+1):
        if santa_alive[i]:
            santa_score[i] += 1

def can_go(x,y):
    return in_range(x,y) and grid[x][y] <= 0

def log(name,variable):
    if DEBUG:
        print(name,end=' ')
        print(variable)

def log_name(name):
    if DEBUG:
        print(name)

###################################################

print_grid()

for k in range(M):
    log("######################## turn",k)

    move_rudolph()
    log_name("after move_rudolph")
    print_grid()
    log("rudol_x",rudol_x)
    log("rudol_y",rudol_y)

    move_santas()
    log_name("after move_santas")
    print_grid()
    log_name(santa_loc)
    log_name(santa_stun)

    wake_santas()
    log_name("after wake_santas")
    log_name(santa_stun)

    if is_ended():
        log_name("all died")
        break

    get_point()
    log_name(santa_score)


log_name("################# ended ##################")

for i in range(1,P+1):
    print(santa_score[i], end=' ')