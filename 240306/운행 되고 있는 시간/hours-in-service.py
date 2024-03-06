N = int(input())
employees = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    temp = [0 for _ in range(1001)]
    for j in range(N):
        if j == i:
            continue
        s, e = employees[j]
        for t in range(s,e):
            temp[t] = 1
    ans = max(ans,sum(temp))

print(ans)