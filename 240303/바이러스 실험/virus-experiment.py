N, M, K = map(int,input().split())


dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

add_nutrition_grid = [list(map(int,input().split())) for i in range(N)]
nutrition_grid = [[5 for i in range(N)] for j in range(N)]
dead_grid = [[[] for i in range(N)] for j in range(N)]
virus_grid = [[[] for i in range(N)] for j in range(N)]

for i in range(M):
    r, c, y = map(int,input().split())
    virus_grid[r-1][c-1].append(y)

############################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_ans():
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += len(virus_grid[i][j])
    print(sum)

def feed():

    for x in range(N):
        for y in range(N):

            # 바이러스가 없으면 넘어갑니다
            if not virus_grid[x][y]:
                continue

            # 어린순으로 먹기 위해 정렬합니다.
            if len(virus_grid[x][y]) > 1:
                virus_grid[x][y].sort()

            new_virus = []
            for v in virus_grid[x][y]:
                if nutrition_grid[x][y] >= v:
                    nutrition_grid[x][y] -= v
                    new_virus.append(v+1)
                else:
                    dead_grid[x][y].append(v)

            virus_grid[x][y] = new_virus

    return

def clear_dead_grid():
    for i in range(N):
        for j in range(N):
            dead_grid[i][j].clear()

def nutrizing():

    for x in range(N):
        for y in range(N):
            for v in dead_grid[x][y]:
                nutrition_grid[x][y] += v//2

    return

def spread():

    new_virus = [[[] for i in range(N)] for j in range(N)]

    for x in range(N):
        for y in range(N):
            for v in virus_grid[x][y]:
                if v % 5 == 0:
                    for dx, dy in zip(dxs,dys):
                        nx,ny = x+dx, y+dy
                        if in_range(nx,ny):
                            new_virus[nx][ny].append(1)

    for x in range(N):
        for y in range(N):
            virus_grid[x][y] += new_virus[x][y]

    return

def add_nutrition():
    for i in range(N):
        for j in range(N):
            nutrition_grid[i][j] += add_nutrition_grid[i][j]
    return

def print_grids():
    for i in range(N):
        for j in range(N):
            print(nutrition_grid[i][j],end=' ')
        print('\t\t',end=' ')
        for j in range(N):
            print(virus_grid[i][j],end=' ')
        print()
    print()

############################################

#print_grids()
for _ in range(K):
    clear_dead_grid()

    feed()
    #print("after feed")
    #print_grids()

    nutrizing()
    #print("after nutrizing")
    #print_grids()

    spread()
    #print("after spread")
    #print_grids()

    add_nutrition()
    #print("after add nutirion")
    #print_grids()

print_ans()