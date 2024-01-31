grid = []
locations = []
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

#################################

def find_locations():
    for i in range(N*N+1):
        locations.append((0,0))
    for i in range(N):
        for j in range(N):
           locations[grid[i][j]] = (i,j)

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def change(x,y):

    global grid,locations

    cur_num = grid[x][y]
    max_num = -1
    max_dir = -1
    for i in range(8):
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx,ny):
            if grid[nx][ny] > max_num:
                max_num = grid[nx][ny]
                max_dir = i
    # 최대 방향이 정해짐
    nx = x + dxs[max_dir]
    ny = y + dys[max_dir]
    grid[x][y] = max_num
    grid[nx][ny] = cur_num

    #locations도 바꿔야 함
    temp_loc = locations[cur_num]
    locations[cur_num] = locations[max_num]
    locations[max_num] = temp_loc

#################################

N, M = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))

find_locations()
#print(locations)

for _ in range(M):
    for num in range(1,N*N+1):
        x,y = locations[num]
        change(x,y)
        #print_grid()
        #print()

#print('-------------------')
print_grid()