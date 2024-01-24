N, T = map(int,input().split())

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

x,y = N//2, N//2
direct = 0
ans = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<N

commands = input()

grid = []

for _ in range(N):
    grid.append(list(map(int,input().split())))

ans = ans + grid[x][y]

for command in commands:
    if command == 'R':
        direct = (direct + 1) % 4
    elif command == 'L':
        direct = (direct + 4 - 1) % 4
    else:
        nx = x + dxs[direct]
        ny = y + dys[direct]
        
        if in_range(nx,ny):
            x = nx
            y = ny
            ans = ans + grid[x][y]

print(ans)