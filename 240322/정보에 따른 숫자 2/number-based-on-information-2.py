T, a, b = map(int,input().split())
pos = [0 for i in range(1001)]
for i in range(T):
    A, x = input().split()
    x = int(x)
    if A == 'S':
        pos[x] = 1
    else:
        pos[x] = 2

def in_range(x):
    return 1<=x<=1000


ans = 0
for k in range(a,b+1):
    ux = k
    dx = k
    while pos[ux] == 0 and pos[dx] == 0:
        nux = ux + 1
        if in_range(nux):
            ux = nux
        ndx = dx - 1
        if in_range(ndx):
            dx = ndx
    if pos[ux] == 1 or pos[dx] == 1:
        ans += 1

print(ans)