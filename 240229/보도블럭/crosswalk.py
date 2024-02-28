N, L = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
ans = 0
#############################
def can_walk(A):
    ramp = [0 for i in range(N)]
    check1, ramp = can_walk_one(A,ramp)
    if not check1:
        return False
    B = []
    ramp2 = []
    for i in range(N-1,-1,-1):
        B.append(A[i])
        ramp2.append(ramp[i])
    check2, _ = can_walk_one(B,ramp2)
    return check2

def can_walk_one(A,ramp):
    prev = A[0]
    combo_start = 0
    combo = 1
    for i in range(1, N):
        cur = A[i]
        if cur == prev:
            prev = cur
            combo += 1
            continue
        elif cur > prev + 1:  # 두칸 이상 높아졌으면
            return False, ramp
        elif cur < prev - 1:
            return False, ramp  # 두칸 이상 낮아졌으면
        elif cur > prev:  # 한칸만 높아졌으면
            if combo >= L:

                # 램프설치
                for c in range(L):
                    cur_ramp = i - 1 - c
                    if ramp[cur_ramp]:
                        return False, ramp
                    ramp[cur_ramp] = 1

                prev = cur
                combo = 1
                combo_start = i
                continue
            else:
                return False, ramp
        elif cur < prev:  # 한칸만 낮아졌으면
            prev = cur
            combo = 1
            combo_start = i
            continue

    return True, ramp

#############################

for i in range(N):
    arr = []
    for j in range(N):
        arr.append(grid[i][j])
    if can_walk(arr):
        #print(arr)
        ans += 1

for j in range(N):
    arr = []
    for i in range(N):
        arr.append(grid[i][j])
    if can_walk(arr):
        #print(arr)
        ans += 1

print(ans)