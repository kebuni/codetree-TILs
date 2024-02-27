# N = int(input())
#
# ans = 0
#
# work = [tuple(map(int,input().split())) for _ in range(N)]
#
# def choose(n,finish,profit_sum):
#     global ans
#     if n == N:
#         ans = max(ans,profit_sum)
#         return
#
#     t, p = work[n]
#     if n >= finish and n+t <= N:
#         choose(n+1,n+t,profit_sum+p)
#     choose(n+1,finish,profit_sum)
#
#     return
#
# choose(0,0,0)
#
# print(ans)

N = int(input())
s = [0 for i in range(N+1)]
e = [0 for i in range(N+1)]
p = [0 for i in range(N+1)]
dp = [-1 for i in range(N+1)] # dp[i] i째일을 마지막으로 선택했을때 가능한 최대 수익
dp[0] = 0

for i in range(1,N+1):
    time, profit = map(int,input().split())
    s[i] = i
    e[i] = i + time - 1
    p[i] = profit

for i in range(1,N+1):
    if e[i] > N:
        continue
    for j in range(i):
        if e[j] < s[i]:
            dp[i] = max(dp[i],dp[j] + p[i])

ans = 0
for i in range(N+1):
    ans = max(ans,dp[i])

print(ans)