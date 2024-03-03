N, K = map(int,input().split())
arr = list(map(int,input().split()))

ans = -1

for i in range(N-K+1):
    sum = 0
    for j in range(K):
        sum += arr[i+j]
    ans = max(ans,sum)

print(ans)