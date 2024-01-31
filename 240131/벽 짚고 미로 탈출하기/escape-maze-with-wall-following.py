grid = []
ans = -1
move_cnt = 0
direct = 0
limit = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

#############################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def is_there_wall(x,y,direct):
    nx = x + dxs[direct]
    ny = y + dys[direct]
    #assert(in_range(nx,ny))
    if not in_range(nx,ny):
        return False
    return grid[nx][ny] == '#'

#############################

N = int(input())
limit = N**3
start_x, start_y = map(int,input().split())
cur_x = start_x - 1
cur_y = start_y - 1

for _ in range(N):
    grid.append(input())

for _ in range(limit):

    # 내 앞에 벽이 있는가?
    wall_test = 0
    while True:
        if is_there_wall(cur_x,cur_y,direct):
            direct = (direct+1)%4
            wall_test += 1
            if wall_test == 4:
                break
        else:
            break
    if wall_test == 4:
        break

    nx = cur_x + dxs[direct]
    ny = cur_y + dys[direct]

    if not in_range(nx,ny):
        move_cnt += 1
        ans = move_cnt
        break
    
    if is_there_wall(nx,ny,(direct+1)%4):
        cur_x = nx
        cur_y = ny
        move_cnt += 1
    else:
        direct = (direct+1) % 4
        cur_x = nx + dxs[direct]
        cur_y = ny + dys[direct]
        move_cnt += 2

print(ans)