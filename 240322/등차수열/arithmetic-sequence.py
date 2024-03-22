N = int(input())
arr = list(map(int,input().split()))
ans = 0
for k in range(min(arr),max(arr)+1):
    temp = 0
    for i in range(N):
        for j in range(i+1,N):
            if arr[j] - k == k - arr[i]:
                temp += 1
    ans = max(ans,temp)
print(ans)