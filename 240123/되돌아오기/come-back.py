d = {}
d['N'] = [-1, 0]
d['E'] = [0, 1]
d['S'] = [1, 0]
d['W'] = [0, -1]

x, y = 0, 0
answer = 0
isPossible = False
isStart = True
N = int(input())

for _ in range(N):
    direction, dist = input().split()
    dist = int(dist)

    nx = x + d[direction][0] * dist
    ny = y + d[direction][1] * dist

    if not isStart:
        if x == 0 and y * ny <= 0:
            answer = answer + abs(y)
            isPossible = True
            break
        if y == 0 and x * nx <= 0:
            answer = answer + abs(x)
            isPossible = True
            break

    x = nx
    y = ny
    answer = answer + dist
    isStart = False
    #print(answer)

if isPossible:
    print(answer)
else:
    print(-1)