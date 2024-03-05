N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

ans = -1

def check(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if grid[i][j] <= 0:
                return False
    return True

for x1 in range(N):
    for y1 in range(M):
        for x2 in range(x1,N):
            for y2 in range(y1,M):
                if check(x1,y1,x2,y2):
                    ans = max(ans,(x2-x1+1)*(y2-y1+1))

print(ans)