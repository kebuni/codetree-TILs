N, S = map(int,input().split())

arr = list(map(int,input().split()))
ans = 987654321
arr_sum = sum(arr)

for i in range(N):
    for j in range(i+1,N):
        ans = min(ans, abs(S - (arr_sum - arr[i] - arr[j])))

print(ans)