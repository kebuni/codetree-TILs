N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

ans = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def check_validity(x,y,r,l):
    return in_range(x-r,y+r) and in_range(x-l,y-l) and in_range(x-r-l,y+r-l)

def get_sum(x,y,r,l):

    dxs = [-1,-1,1,1]
    dys = [1,-1,-1,1]
    dist = [r,l,r,l]

    sum = 0
    
    for i in range(4):
        for k in range(dist[i]):
            x = x + dxs[i]
            y = y + dys[i]
            sum += grid[x][y]
    
    return sum

for x in range(2,N):
    for y in range(1,N-1):
        for r in range(1,N):
            for l in range(1,N):
                if check_validity(x,y,r,l):
                    ans = max(ans,get_sum(x,y,r,l))

print(ans)