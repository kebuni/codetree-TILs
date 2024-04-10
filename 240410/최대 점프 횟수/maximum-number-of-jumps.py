N = int(input())
arr = list(map(int,input().split()))
dp = [-1 for i in range(N)]
dp[0] = 0
for i in range(1,N):
    temp = -1
    for j in range(i):
        if dp[j] != -1 and j+arr[j] >= i:
            # print("j",j,"arr[j]",arr[j])
            temp = max(temp,dp[j]+1)
    
    dp[i] = temp

print(max(dp))