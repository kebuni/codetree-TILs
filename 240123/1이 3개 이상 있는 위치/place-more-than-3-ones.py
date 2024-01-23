import sys

N = int(input())

# x,y = 0,0
cnt = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

###########

grid = []

for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

for x in range(N):
    for y in range(N):
        one_num = 0
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                one_num = one_num + 1
        if one_num >= 3:
            cnt = cnt + 1

print(cnt)