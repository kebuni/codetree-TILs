N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
ans = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

#####################

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def find_max(x,y):
    visited = [(x,y)]
    dfs(x,y,0,grid[x][y],visited)
    return

def dfs(x,y,n,value,visited):
    # print(x,y,n,value,visited)
    global ans
    if n == 3:
        ans = max(ans,value)
        return

    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,n+1,value+grid[nx][ny],visited)
            visited.pop()
    return


#####################

for x in range(N):
    for y in range(M):
        find_max(x,y)
        # print("x,y",x,y,ans)

print(ans)