grid = []
visited = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
town = [0]
town_grid = []
town_num = 0
###############################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(town_grid[i][j],end=' ')
        print()

def dfs(x,y):
    global town_grid, town, visited

    visited[x][y] = True
    town_grid[x][y] = town_num
    town[town_num] += 1
    
    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny):
            dfs(nx,ny)

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 0:
        return False
    return True    

###############################
N = int(input())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    town_grid.append([0 for i in range(N)])
    visited.append([False for i in range(N)])

for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j]:
            #새로운 마을을 찾았다!
            town_num += 1
            town.append(0)
            dfs(i,j)

#print_grid()
#print(town)

town.sort()
print(town_num)
for i in range(1,town_num+1):
    print(town[i])