N = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(N)]

for i in range(1,N):
    temp = -1
    for j in range(i):
        if arr[j] < arr[i]:
            temp = max(temp,dp[j])
    dp[i] = temp + 1

print(max(dp)+1)