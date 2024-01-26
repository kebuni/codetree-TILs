n = int(input())

grid = []

dxs = [-1,-1,1,1]
dys = [1,-1,-1,1]

max = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def make_rec(origin_x,origin_y):
    x = origin_x
    y = origin_y
    sum = 0
    direct = 0

    while(1):
        nx = x + dxs[direct]
        ny = y + dys[direct]
        if in_range(nx,ny):
            x = nx
            y = ny
            sum = sum + grid[x][y]
        else:
            direct = direct + 1
        
        if direct == 4:
            break
    return sum
    

for _ in range(n):
    grid.append(list(map(int,input().split())))

for i in range(1,n-1):
    temp = make_rec(n-1,i)
    if temp > max:
        max = temp

print(max)