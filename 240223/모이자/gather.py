ans = 987654321

N = int(input())
arr = list(map(int,input().split()))

for i in range(N):
    sum = 0
    for j in range(N):
        sum += abs(i-j) * arr[j]
    ans = min(ans,sum)

print(ans)