import sys
sys.setrecursionlimit(9999)

# 원래 코드 


grid = []
visited = []
#safezone_grid = []
highest = -1
safezone_num = 0
K = 0

ans_K = -1
ans_num = -1

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
#######################

def clear_visited():
    global visited
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] <= K:
        return False
    return True

def dfs(x,y):
    global visited, safezone_num
    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny):
            visited[nx][ny] = True
            #safezone_grid[nx][ny] = safezone_num
            dfs(nx,ny)

    return


#######################

N, M = map(int,input().split())
for _ in range(N):
    grid_list = list(map(int,input().split()))
    for h in grid_list:
        highest = max(highest,h)
    grid.append(grid_list)
    visited.append([False for i in range(M)])
    #safezone_grid.append([0 for i in range(M)])

for k in range(1,highest+1):
    K = k
    
    # 물의 높이 각 k에 대하여...
    clear_visited()
    safezone_num = 0

    for i in range(N):
        for j in range(M):
            # 새로운 safezone을 찾았다!
            if not visited[i][j] and grid[i][j] > k:
                visited[i][j] = True
                safezone_num += 1
                #safezone_grid[i][j] = safezone_num
                dfs(i,j)

    #탐색이 끝남
    if safezone_num > ans_num:   
        ans_num = safezone_num
        ans_K = k
        #print("new score!!",ans_K,ans_num)

print(ans_K,end=' ')
print(ans_num)