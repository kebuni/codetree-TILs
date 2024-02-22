ans = -1

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N-2):
        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        ans = max(ans,sum)

print(ans)