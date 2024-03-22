N, K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

def in_range(x):
    return 0<=x<N

ans = -1
for x in range(N):
    cur = arr[x]
    for j in range(-K,K+1):
        if j == 0:
            continue
        nx = x + j
        if in_range(nx):
            if cur == arr[nx]:
                ans = max(ans,cur)

print(ans)