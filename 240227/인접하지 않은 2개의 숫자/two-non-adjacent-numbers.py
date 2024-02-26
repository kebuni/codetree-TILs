N = int(input())

ans = 0

arr = list(map(int,input().split()))

for i in range(N):
    for j in range(i+2,N):
        ans = max(ans,arr[i]+arr[j])

print(ans)