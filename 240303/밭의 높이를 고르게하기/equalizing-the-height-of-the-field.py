N, H, T = map(int,input().split())
arr = list(map(int,input().split()))

ans = 987654321

for i in range(N-T+1):
    sum = 0
    for j in range(T):
        sum += abs(arr[i+j] - H)
    ans = min(ans,sum)

print(ans)