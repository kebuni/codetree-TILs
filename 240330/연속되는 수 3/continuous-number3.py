N = int(input())
arr = [int(input()) for i in range(N)]

ans, cnt = 0, 0
for i in range(N):
    if i > 0 and arr[i]*arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)
print(ans)