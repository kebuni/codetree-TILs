N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
ans = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

visited = []

#####################

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and (x,y) not in visited

def find_max(n,value):
    global ans
    if n == 4:
        ans = max(ans,value)
        return

    for (x,y) in visited:
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                visited.append((nx,ny))
                find_max(n+1,value + grid[nx][ny])
                visited.pop()

    return


#####################

for x in range(N):
    for y in range(M):
        visited.append((x,y))
        find_max(1,grid[x][y])
        visited.pop()

print(ans)