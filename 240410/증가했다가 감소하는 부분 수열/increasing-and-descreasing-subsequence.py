N = int(input())
arr = list(map(int,input().split()))
dp1 = [1 for i in range(N)]
dp2 = [1 for i in range(N)]

for i in range(1,N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp1[i] = max(dp1[i],dp1[j]+1)

for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i]>arr[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)

# print(dp1)
# print(dp2)

print(max([dp1[i]+dp2[i]-1 for i in range(N)]))