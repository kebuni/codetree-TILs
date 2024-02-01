grid = []
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

#grid2 = [[[],[],[4]],[[2],[1,7,6],[3]],[[9],[8],[5]]]

##################

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def find_location():
    global locations
    for i in range(N):
        for j in range(N):
            num = grid[i][j][0]
            locations[num] = (i,j)

def find_max(x,y):
    max_num = -1
    max_dir = -1
    max_idx = -1
    for i in range(8):
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx,ny): #격자 안이면
            for k in range(len(grid[nx][ny])):
                if grid[nx][ny][k] > max_num:
                    max_num = grid[nx][ny][k]
                    max_dir = i
                    max_idx = k
    return max_num, max_dir, max_idx

def print_ans():
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]):
                for k in range(len(grid[i][j])-1,-1,-1):
                    print(grid[i][j][k],end=' ')
                print()
            else:
                print("None")


##################
N, M = map(int,input().split())
for _ in range(N):
    grid.append(list(map(lambda x:[int(x)],input().split())))

nums = list(map(int,input().split()))
locations = [(0,0) for i in range(N*N+1)]

find_location()

for num in nums:

    # print_grid()
    # print(locations)
    # print()

    cur_idx = -1
    x,y = locations[num]
    for i in range(len(grid[x][y])):
        if grid[x][y][i] == num:
            cur_idx = i
            break


    max_num, max_dir, max_idx = find_max(x,y)
    if max_dir == -1: #만약 max_dir이 -1이면 주변에 숫자가 하나도 없음
        continue

    temp = grid[x][y][cur_idx:]
    grid[x][y] = grid[x][y][:cur_idx]

    nx = x+dxs[max_dir]
    ny = y+dys[max_dir]
    #temp2 = grid[nx][ny][max_idx:]
    #grid[nx][nx] = grid[nx][ny][:max_idx]

    for elem in temp:
        locations[elem] = (nx,ny)
    #for elem in temp2:
    #    locations[elem] = (x,y)

    #grid[x][y] += temp2
    grid[nx][ny] += temp

#print_grid()
#print()
print_ans()