N, M, T = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
delta = [[0 for i in range(M)] for j in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

upper_x = -1
down_x = -1

for x in range(N):
    if grid[x][0] == -1:
        upper_x = x
        down_x = x+1
        break

#########################################

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and grid[x][y] != -1

def clear_delta():
    for i in range(N):
        for j in range(M):
            delta[i][j] = 0

def dust_sum():
    sum = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] != -1:
                sum += grid[i][j]
    return sum

def print_grid():
    for i in range(N):
        for j in range(M):
            print(grid[i][j],end=' ')
        print()
    print()

def spread():

    for x in range(N):
        for y in range(M):

            if grid[x][y] <= 0:
                continue

            # (x,y)의 먼지를 퍼트리겠습니다.
            for dx, dy in zip(dxs,dys):
                nx, ny = x + dx, y + dy
                if can_go(nx,ny):
                    dust = grid[x][y] // 5
                    delta[nx][ny] += dust
                    delta[x][y] -= dust

    for x in range(N):
        for y in range(M):
            grid[x][y] += delta[x][y]

    return

def clean():

    # 돌풍 윗쪽의 반시계 -> 돌풍 윗칸부터 앞에거를 가져와야 함
    x = upper_x - 1
    y = 0
    d = 0
    while grid[x][y] != -1:
        nx, ny = x + dxs[d], y + dys[d]
        if in_range_upper(nx,ny):
            if grid[nx][ny] == -1:
                grid[x][y] = 0
            else:
                grid[x][y] = grid[nx][ny]
            x, y = nx, ny
        else:
            d = (d+1) % 4

    x = down_x + 1
    y = 0
    d = 2
    # 돌풍 아랫쪽의 시계 -> 돌풍 아랫칸부터 앞에거를 가져와야 함
    while grid[x][y] != -1:
        nx, ny = x + dxs[d], y + dys[d]
        if in_range_down(nx, ny):
            if grid[nx][ny] == -1:
                grid[x][y] = 0
            else:
                grid[x][y] = grid[nx][ny]
            x, y = nx, ny
        else:
            d = (d - 1 + 4) % 4

    return

def in_range_upper(x,y):
    return 0<=x<= upper_x and 0<=y<M

def in_range_down(x,y):
    return down_x <= x < N and 0<=y<M

#########################################

for _ in range(T):
    clear_delta()

    spread()
    #print("after spread")
    #print_grid()

    clean()
    # print("after clean")
    # print_grid()
    #
    # print(dust_sum())

print(dust_sum())