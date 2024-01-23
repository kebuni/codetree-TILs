dxs = [-1,0,0,1]
dys = [0,1,-1,0]

directions = {}
directions['U'] = 0
directions['R'] = 1
directions['L'] = 2
directions['D'] = 3

#####################################

n, t = map(int,input().split())
r, c, d = input().split()
x = int(r)
y = int(c)
direction = directions[d]

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

for _ in range(t):

    #print(x,y,direction)

    nx = x + dxs[direction]
    ny = y + dys[direction]

    if in_range(nx,ny):
        x = nx
        y = ny
        continue
    else:
        direction = 3 - direction
        continue

########################################

print(x,y,end=' ')