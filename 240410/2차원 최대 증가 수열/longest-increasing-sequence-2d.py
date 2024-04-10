N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
dp = [[-1 for i in range(M)] for j in range(N)]
dp[0][0] = 0

for y in range(1,M):
    dp[0][y] = 0

for x in range(1,N):
    dp[x][0] = 0

for x in range(1,N):
    for y in range(1,M):
        for i in range(x):
            for j in range(y):
                if dp[i][j] != -1 and grid[i][j] < grid[x][y]:
                    dp[x][y] = max(dp[x][y],dp[i][j]+1)

# for x in range(N):
#     for y in range(M):
#         print(dp[x][y],end=' ')
#     print()

ans = 0
for x in range(N):
    for y in range(M):
        ans = max(ans,dp[x][y])

print(ans+1)