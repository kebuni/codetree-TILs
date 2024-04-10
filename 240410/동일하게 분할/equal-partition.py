OFFSET = 100000
N = int(input())
arr = list(map(int,input().split()))
arr = [0]+arr

dp = [[False for i in range(OFFSET + 100000 + 1)] for j in range(N+1)]
dp[0][OFFSET + 0] = True

for i in range(1,N+1):
    for j in range(-100000,100000+1):
        if dp[i-1][j+OFFSET]:
            #print("i-1,j",i-1,j)
            dp[i][j+OFFSET+arr[i]] = True
            dp[i][j+OFFSET-arr[i]] = True

if dp[N][0+OFFSET]:
    print("Yes")
else:
    print("No")