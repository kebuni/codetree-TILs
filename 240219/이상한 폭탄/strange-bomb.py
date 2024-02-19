N, K = map(int,input().split())
s = {}
arr = []
ans = -1

for i in range(N):
    arr.append(int(input()))

for i in range(K):
    if arr[i] in s and s[arr[i]]:
        ans = max(ans,arr[i])
    if arr[i] in s:
        s[arr[i]] += 1
    else:
        s[arr[i]] = 1

for i in range(K,N):
    if arr[i] in s and s[arr[i]]:
        ans = max(ans,arr[i])
    s[arr[i-K]] -= 1
    if arr[i] in s:
        s[arr[i]] += 1
    else:
        s[arr[i]] = 1

print(ans)