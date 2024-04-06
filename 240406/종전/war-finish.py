import sys

N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
boundary = [[False for i in range(N)] for j in range(N)]
ans = sys.maxsize

dxs = [-1,-1,1,1]
dys = [1,-1,-1,1]
####################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def possible(x,y,r,l):
    if not in_range(x-r,y+r):
        return False
    if not in_range(x-r-l,y+r-l):
        return False
    if not in_range(x-l,y-l):
        return False
    return True

def clear_boundary():
    for x in range(N):
        for y in range(N):
            boundary[x][y] = False

def draw_boundary(x,y,r,l):
    clear_boundary()
    dist = [r,l,r,l]
    for d in range(4):
        for i in range(dist[d]):
            boundary[x][y] = True
            x, y = x + dxs[d], y + dys[d]

    return

def get_diff(x,y,r,l):
    global ans
    draw_boundary(x,y,r,l)
    population = [0,0,0,0,0]

    # 2번부족
    for i in range(x-l):
        for j in range(y+r-l+1):
            if boundary[i][j]:
                break
            population[1] += grid[i][j]

    # 3번부족
    for i in range(x-r+1):
        for j in range(N-1,y+r-l,-1):
            if boundary[i][j]:
                break
            population[2] += grid[i][j]

    # 4번부족
    for i in range(x-l,N):
        for j in range(y):
            if boundary[i][j]:
                break
            population[3] += grid[i][j]

    # 5번부족
    for i in range(x-r+1,N):
        for j in range(N-1,y-1,-1):
            if boundary[i][j]:
                break
            population[4] += grid[i][j]

    # 1번부족
    population[0] = total_population - sum(population)
    ans = min(ans,max(population)-min(population))

    # print(x,y,r,l)
    # print(population)
    # print(ans)
    return

def print_boundary():
    for x in range(N):
        for y in range(N):
            print(1 if boundary[x][y] else 0,end=' ')
        print()
    print()

####################################################

total_population = sum([grid[x][y] for x in range(N) for y in range(N)])

for x in range(2,N):
    for y in range(1,N-1):
        for r in range(1,N):
            for l in range(1,N):
                if possible(x,y,r,l):
                    get_diff(x,y,r,l)

print(ans)