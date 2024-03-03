N, M = map(int,input().split())

A = list(map(int,input().split()))
B = set(map(int,input().split()))

ans = 0

for i in range(N-M+1):
    S = set()
    for k in range(M):
        S.add(A[i+k])
    if S == B:
        ans += 1

print(ans)