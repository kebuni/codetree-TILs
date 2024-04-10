N = int(input())
work = [tuple(map(int,input().split())) for i in range(N)]
dp = [work[i][2] for i in range(N)]

def overlap(j,i):
    sj, ej, _ = work[j]
    si, ei, _ = work[i]
    return si <= ej

for i in range(1,N):
    for j in range(i):
        if not overlap(j,i):
            dp[i] = max(dp[i],dp[j]+work[i][2])

# print(dp)
print(max(dp))