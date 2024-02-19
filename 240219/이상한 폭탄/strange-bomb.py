N, K = map(int,input().split())
s = set()
arr = []
ans = -1

for i in range(N):
    arr.append(int(input()))

for i in range(K):
    s.add(arr[i])

for i in range(K,N):
    if arr[i] in s:
        ans = max(ans,arr[i])
    s.remove(arr[i-K])
    s.add(arr[i])

print(ans)