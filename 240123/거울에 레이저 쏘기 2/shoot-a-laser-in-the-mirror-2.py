import sys

N = int(input())

dxs = [-1,1,0,0]
dys = [0,0,1,-1]
direction = -1
x, y = -1, -1
ans = 0

grid = [[1]*N for _ in range(N)]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def reflect(x,y,direction):
    if grid[x][y] == 0:
        if direction > 1:
            return 4 - direction
        else:
            return 2 - direction
    else:
        return 3 - direction

for i in range(N):
    line = sys.stdin.readline()
    for j in range(N):
        if line[j] == '/':
            grid[i][j] = 0

light = int(input())

### 초기 위치와 방향 잡기 ###

if 1<=light<=N:
    direction = 1
    x = 0; y = light - 1
elif N+1<=light<=N*2:
    direction = 3
    y = N-1; x = (light -1 ) % N
elif N*2+1<=light<=N*3:
    direction = 0
    x = N-1; y = (4*N - light) % N
else:
    direction = 2
    y = 0; x = 4*N - light

while in_range(x,y):
    #print(x,y,direction)
    direction = reflect(x,y,direction)
    #print("new_dir: ",direction)
    x = x + dxs[direction]
    y = y + dys[direction]
    ans = ans + 1

print(ans)