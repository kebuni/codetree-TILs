import sys

INT_MAX = sys.maxsize
N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
ans = INT_MAX

for i in range(N):
    outer = [-INT_MAX, INT_MAX, -INT_MAX, INT_MAX]
    for j in range(N):
        
        if i == j:
            continue

        x, y = points[j]
        outer[0] = max(outer[0],x)
        outer[1] = min(outer[1],x)
        outer[2] = max(outer[2],y)
        outer[3] = min(outer[3],y)

    size = (outer[0] - outer[1]) * (outer[2] - outer[3])
    ans = min(ans,size)

print(ans)