import sys
sys.setrecursionlimit(2000)

grid = []
visited = []
blocks = []
max_block_size = -1
cur_block_size = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
#####################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,cur_num):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] != cur_num:
        return False
    return True

def dfs(x,y,cur_num):
    global cur_block_size

    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny,cur_num):
            visited[nx][ny] = True
            cur_block_size += 1
            dfs(nx,ny,cur_num)

    return

#####################
N = int(input())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([False for i in range(N)])

for i in range(N):
    for j in range(N):

        # 가본적 없는 새로운 블럭을 찾았다면...
        if not visited[i][j]:
            cur_block_size = 1
            visited[i][j] = True
            dfs(i,j,grid[i][j])
            
            #블럭 탐색이 끝났다면
            blocks.append(cur_block_size)
        
sum = 0
max_size = 0
for elem in blocks:
    if elem >= 4:
        sum += 1
    max_size = max(max_size,elem)

print(sum,end=' ')
print(max_size)