N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def check_combo(arr):
    prev = arr[0]
    combo = 1
    for i in range(1,N):
        
        if combo == M:
            return True

        # 아직 콤보를 못 채움
        cur = arr[i]
        if prev == cur:
            combo += 1
        else:
            combo = 1
        prev = cur

    if combo == M:
        return True

    return False
        
for x in range(N):
    if check_combo(grid[x]):
        ans += 1

for y in range(N):
    A = []
    for x in range(N):
        A.append(grid[x][y])
    if check_combo(A):
        ans += 1

print(ans)