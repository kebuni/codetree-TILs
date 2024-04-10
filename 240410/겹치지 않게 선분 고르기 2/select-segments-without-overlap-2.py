N = int(input())
lines = [tuple(map(int,input().split())) for i in range(N)]
lines.sort()
dp = [0 for i in range(N)]
dp[0] = 1

def overlap(j,i):
    si, ei = lines[i]
    sj, ej = lines[j]

    return si <= ej

for i in range(1,N):
    for j in range(i):
        if not overlap(j,i):
            dp[i] = max(dp[i],dp[j]+1)

# print(dp)
print(max(dp))