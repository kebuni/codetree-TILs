N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    si, ei = lines[i]
    overlap = False
    for j in range(N):

        if j == i:
            continue

        sj, ej = lines[j]

        if (si <= sj and ei >= ej) or (si >= sj and ei <= ej):
            overlap = True
            break

    if not overlap:
        ans += 1

print(ans)