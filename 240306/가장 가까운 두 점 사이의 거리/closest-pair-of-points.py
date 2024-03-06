import sys

N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
ans = sys.maxsize

def get_dist(i,j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return (x1-x2)**2 + (y1-y2)**2

for i in range(N):
    for j in range(i+1,N):
        ans = min(ans,get_dist(i,j))

print(ans)