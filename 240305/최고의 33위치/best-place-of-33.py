N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

ans = -1

for i in range(N-3+1):
    for j in range(N-3+1):
        sum = 0
        for x in range(3):
            for y in range(3):
                sum += grid[i+x][j+y]
        ans = max(ans,sum)

print(ans)