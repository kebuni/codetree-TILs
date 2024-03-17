N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
#delta = [[0 for i in range(N)] for j in range(N)]

dist_list = []
for i in range(1,N):
    dist_list.append(i)
    dist_list.append(i)
dist_list.append(N-1)

dxs = [0,1,0,-1]
dys = [-1,0,1,0]
out_of_grid_dust = 0
# sweep_info = [(0,-2,0.05),
#               (-1,-1,0.1),
#               (1,-1,0.1),
#               (-2,0,0.02),
#               (-1,0,0.07),
#               (1,0,0.07),
#               (2,0,0.02),
#               (-1,1,0.01),
#               (1,1,0.01)]
sweep_infos = []
dust_ratio = [
    [
        [0,  0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5,  0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0,  0, 2, 0, 0],
    ],
    [
        [0,  0, 0,  0, 0],
        [0,  1, 0,  1, 0],
        [2,  7, 0,  7, 2],
        [0, 10, 0, 10, 0],
        [0,  0, 5,  0, 0],
    ],
    [
        [0, 0, 2,  0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0,  0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2,  0, 0],
    ],
    [
        [0,  0, 5,  0, 0],
        [0, 10, 0, 10, 0],
        [2,  7, 0,  7, 2],
        [0,  1, 0,  1, 0],
        [0,  0, 0,  0, 0],
    ]
]

##########################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def sweep(x,y,d):
    global out_of_grid_dust
    #clear_delta()

    #sweep_grid = get_sweep_grid(d)

    cur_dust = grid[x][y]
    moved_dust = 0
    for dx in range(-2,3):
        for dy in range(-2,3):
            nx,ny = x + dx, y+dy
            if in_range(nx,ny):
                grid[nx][ny] += cur_dust * dust_ratio[d][dx+2][dy+2] // 100
                moved_dust += cur_dust * dust_ratio[d][dx+2][dy+2] // 100
            else:
                out_of_grid_dust += cur_dust * dust_ratio[d][dx+2][dy+2] // 100
                moved_dust += cur_dust * dust_ratio[d][dx + 2][dy + 2] // 100

    nx = x + dxs[d]
    ny = y + dys[d]
    if in_range(nx,ny):
        grid[nx][ny] += cur_dust - moved_dust
    else:
        out_of_grid_dust += cur_dust - moved_dust
    grid[x][y] = 0

    #sum_delta()

    return



# def clear_delta():
#     for x in range(N):
#         for y in range(N):
#             delta[x][y] = 0
#
# def sum_delta():
#     for x in range(N):
#         for y in range(N):
#             grid[x][y] += delta[x][y]

def print_grid():
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()

##########################################

cur_x, cur_y = N//2, N//2
cur_d = 0

for dist in dist_list:
    for i in range(dist):
        cur_x = cur_x + dxs[cur_d]
        cur_y = cur_y + dys[cur_d]
        #print(cur_x,cur_y,cur_d)
        sweep(cur_x,cur_y,cur_d)
        #print_grid()
        #print(out_of_grid_dust)
    cur_d = (cur_d + 1) % 4

print(out_of_grid_dust)