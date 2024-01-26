n = int(input())

grid = []

dxs = [-1,-1,1,1]
dys = [1,-1,-1,1]

ans = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def make_rec(x,y,k,l):
    
    sum = 0
    dists = [k,l,k,l]

    for i in range(4):

        for j in range(dists[i]):
            nx = x+dxs[i]
            ny = y+dys[i]
            if in_range(nx,ny):
                x = nx
                y = ny
                sum = sum + grid[x][y]
            else:
                return 0

    return sum
    

for _ in range(n):
    grid.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                ans = max(ans,make_rec(i,j,k,l))

print(ans)