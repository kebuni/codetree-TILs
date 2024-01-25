n, m = map(int,input().split())

grid = []
grid_col = []
ans = 0

def is_happy(arr):
    cnt = 1
    prev = arr[0]
    
    if m==1: return True
    
    for i in range(1,len(arr)):
        if arr[i] == prev:
            cnt = cnt+1
        else:
            cnt = 1
        prev = arr[i]
        if cnt == m:
            return True
    return False

for i in range(n):
    grid.append(list(map(int,input().split())))

for arr in grid:
    if is_happy(arr):
        ans = ans+1

for i in range(n):
    grid_in = []
    for j in range(n):
        grid_in.append(grid[j][i])
    grid_col.append(grid_in)

for arr in grid_col:
    if is_happy(arr):
        ans = ans+1

print(ans)