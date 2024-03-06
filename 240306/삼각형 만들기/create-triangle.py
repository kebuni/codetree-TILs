N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0

def valid(i,j,k):
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]

    valid_x = (xi-xj) * (xi-xk) * (xj-xk)
    valid_y = (yi-yj) * (yi-yk) * (yj-yk)

    if valid_x == 0 and valid_y == 0:
        return True
    else:
        return False

def get_size(i,j,k):
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]

    xs = [xi,xj,xk]
    ys = [yi,yj,yk]

    return (max(xs) - min(xs)) * (max(ys)-min(ys))

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if valid(i,j,k):
                ans = max(ans,get_size(i,j,k))

print(ans)