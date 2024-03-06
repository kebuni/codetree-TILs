N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    si, ei = lines[i]
    not_overlap = True
    for j in range(N):

        if j == i:
            continue

        sj, ej = lines[j]

        if si <= sj <= ej <= ei:
            not_overlap = False
        if ei <= sj <= ej <= si:
            not_overlap = False
        if si <= ej <= sj <= ei:
            not_overlap = False
        if ei <= ej <= sj <= si:
            not_overlap = False

        if sj <= si <= ei <= ej:
            not_overlap = False
        if ej <= si <= ei <= sj:
            not_overlap = False
        if sj <= ei <= si <= ej:
            not_overlap = False
        if ej <= ei <= si <= sj:
            not_overlap = False

    if not_overlap:
        ans += 1

print(ans)