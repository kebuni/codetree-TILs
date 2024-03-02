N = int(input())
curves = [tuple(map(int,input().split())) for i in range(N)]

dxs = [0,-1,0,1]
dys = [1,0,-1,0]

grid = [[ 0 for i in range(101)] for j in range(101)]

############################

def print_ans():
    sum = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
                sum += 1
    print(sum)

def in_range(x,y):
    return 0<=x<101 and 0<=y<101

def make_curve(x,y,d,g):
    px = x+dxs[d]
    py = y+dys[d]
    coord = [(x,y),(px,py)]
    for i in range(g):
        coord, (px,py) = copy_curve(coord,x,y,(px,py))

    for x, y in coord:
        if in_range(x,y):
            grid[x][y] = 1

    #print_grid()

    return

def copy_curve(A,ix,iy,pivot):
    px, py = pivot
    B = []
    for x, y in A:
        nx = px + (y-py)
        ny = py + (px-x)
        B.append((nx,ny))

    npx = px + (iy - py)
    npy = py + (px - ix)
    return A+B, (npx,npy)

def print_grid():
    for i in range(101):
        for j in range(101):
            print(grid[i][j],end=' ')
        print()
    print()

############################

#print(curves)

for x,y,d,g in curves:
    make_curve(x,y,d,g)

print_ans()