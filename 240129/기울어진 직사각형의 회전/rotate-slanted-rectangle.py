# 행, 열 1시작 조심!

grid = []
ccw_x = [-1,-1,1,1]
ccw_y = [1,-1,-1,1]
cw_x = [-1,-1,1,1]
cw_y = [-1,1,1,-1]

################

def print_grid():

    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def rotate(r,c,m1,m2,direct):

    x,y = r,c
    temp = grid[r][c]

    if direct==0: # 반시계
        cnt = [m2,m1,m2,m1]
        for i in range(4):
            for k in range(cnt[i]):
                nx = x + cw_x[i]
                ny = y + cw_y[i]
                grid[x][y] = grid[nx][ny]
                x = nx
                y = ny
        grid[x-1][y+1] = temp

    else: # 시계
        cnt = [m1,m2,m1,m2]
        for i in range(4):
            for k in range(cnt[i]):
                nx = x + ccw_x[i]
                ny = y + ccw_y[i]
                grid[x][y] = grid[nx][ny]
                x = nx
                y = ny
        grid[x-1][y-1] = temp


################

N = int(input())

for _ in range(N):
    grid.append(list(map(int,input().split())))

R, C, m1, m2, _, _, direct = map(int,input().split())

rotate(R-1,C-1,m1,m2,direct)

print_grid()