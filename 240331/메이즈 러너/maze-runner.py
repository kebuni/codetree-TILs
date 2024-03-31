N, M, K = map(int,input().split())
player = [[[] for i in range(N)] for j in range(N)]
next_player = [[[] for i in range(N)] for j in range(N)]
wall = [list(map(int,input().split())) for i in range(N)]
for i in range(1,M+1):
    x, y = map(int,input().split())
    player[x-1][y-1].append(i)
exit_x, exit_y = map(int,input().split())
exit_x -= 1
exit_y -= 1
wall[exit_x][exit_y] = -1

move_num = 0
###################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def can_go(x,y):
    return in_range(x,y) and wall[x][y] <= 0

def print_grid(grid):
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()
    return

def check_end():
    for x in range(N):
        for y in range(N):
            if player[x][y]:
                return False
    return True

def move_all():
    global move_num
    clear_next()

    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    for x in range(N):
        for y in range(N):
            for p in player[x][y]:

                # player p를 이동시킵니다.
                next_x, next_y = x, y
                min_dist = dist(x,y,exit_x,exit_y)
                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if can_go(nx,ny):
                        temp_dist = dist(nx,ny,exit_x,exit_y)
                        if temp_dist < min_dist:
                            min_dist = temp_dist
                            next_x, next_y = nx, ny

                # 다음 위치가 선정되었습니다.

                # 한칸 이동 했다면 move_num을 더해줍니다.
                if (next_x, next_y) != (x,y):
                    move_num += 1

                # 다음 칸이 출구가 아니라면 next에 넣어줍니다.
                if (next_x, next_y) != (exit_x, exit_y):
                    next_player[next_x][next_y].append(p)


    copy_next()
    return

def clear_next():
    for x in range(N):
        for y in range(N):
            next_player[x][y].clear()
    return

def copy_next():
    for x in range(N):
        for y in range(N):
            player[x][y] = next_player[x][y][:]
    return

def find_min_square():
    best = (1000,1000,1000)

    for x in range(N):
        for y in range(N):
            if player[x][y]:
                temp = find_min_length(x,y,exit_x,exit_y)
                if temp < best:
                    best = temp

    length, lux, luy = best
    return lux, luy, length

def find_min_length(x,y,ex,ey):
    length = max(abs(x-ex)+1, abs(y-ey)+1)
    lux = max(ex-length+1,x-length+1)
    luy = max(ey-length+1,y-length+1)
    if lux < 0:
        lux = 0
    if luy < 0:
        luy = 0
    return (length,lux,luy)

def rotate(lux,luy,l):
    # player 회전
    temp = [[[] for i in range(l)] for j in range(l)]
    for i in range(l):
        for j in range(l):
            temp[j][(l-1)-i] = player[lux+i][luy+j][:]
    for i in range(l):
        for j in range(l):
            player[lux+i][luy+j] = temp[i][j][:]
    # wall 회전. 이때 0보다 크다면 -1하면서 회전
    temp = [[-2 for i in range(l)] for j in range(l)]
    for i in range(l):
        for j in range(l):
            temp[j][(l - 1) - i] = wall[lux + i][luy + j]
    for i in range(l):
        for j in range(l):
            if temp[i][j] > 0:
                wall[lux + i][luy + j] = temp[i][j] - 1
            else:
                wall[lux + i][luy + j] = temp[i][j]
    return

def print_ans():
    print(move_num)
    print(exit_x+1, exit_y+1)
    return

def update_exit_pos():
    global exit_x, exit_y
    for x in range(N):
        for y in range(N):
            if wall[x][y] == -1:
                exit_x = x
                exit_y = y
                break
    return

###################################

# print("beginning")
# print_grid(player)
# print_grid(wall)

for t in range(K):

    # print('--------------------',t)

    update_exit_pos()
    # print("exit:", exit_x, exit_y)

    if check_end():
        # print("all player done")
        break

    move_all()
    # print("after move all")
    # print("move num:", move_num)
    # print_grid(player)

    lux, luy, length = find_min_square()
    # print("lux, luy, length : ", lux, luy, length)
    # print()

    rotate(lux,luy,length)
    # print("after rotate")
    # print_grid(player)
    # print_grid(wall)

update_exit_pos()
print_ans()