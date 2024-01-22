x = 0
y = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]

N = int(input())

for _ in range(N):
    direction, dist = input().split()

    if direction == 'W':
        x = x + int(dist) * dx[0]
        y = y + int(dist) * dy[0]
    elif direction == 'S':
        x = x + int(dist) * dx[1]
        y = y + int(dist) * dy[1]
    elif direction == 'N':
        x = x + int(dist) * dx[2]
        y = y + int(dist) * dy[2]
    else:
        x = x + int(dist) * dx[3]
        y = y + int(dist) * dy[3]

print(str(x),str(y),end=' ')