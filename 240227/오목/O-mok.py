import sys

N = 19
NOPE = 0
BLACK = 1
WHITE = 2

grid = [list(map(int, input().split())) for i in range(N)]

combo = [0, 0, 0]
last = NOPE


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


for i in range(N):
    combo = [0, 0, 0]
    for j in range(N):
        cur = grid[i][j]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(i + 1, j - 2 + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(i + 1, j - 2 + 1)
            sys.exit(0)

for j in range(N):
    combo = [0, 0, 0]
    for i in range(N):
        cur = grid[i][j]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(i - 2 + 1, j + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(i - 2 + 1, j + 1)
            sys.exit(0)

for i in range(N):
    x = 0
    y = i
    combo = [0, 0, 0]
    while in_range(x, y):
        cur = grid[x][y]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(x - 2 + 1, y + 2 + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(x - 2 + 1, y + 2 + 1)
            sys.exit(0)

        x += 1
        y -= 1
for i in range(1, N):
    x = i
    y = N - 1
    combo = [0, 0, 0]
    while in_range(x, y):
        cur = grid[x][y]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(x - 2 + 1, y + 2 + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(x - 2 + 1, y + 2 + 1)
            sys.exit(0)

        x += 1
        y -= 1

for i in range(N - 1, -1, -1):
    x = 0
    y = i
    combo = [0, 0, 0]
    while in_range(x, y):
        cur = grid[x][y]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(x - 2 + 1, y - 2 + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(x - 2 + 1, y - 2 + 1)
            sys.exit(0)

        x += 1
        y += 1
for i in range(1, N):
    x = i
    y = 0
    combo = [0, 0, 0]
    while in_range(x, y):
        cur = grid[x][y]
        if last == cur:
            combo[cur] += 1
        else:
            combo[cur] = 1
            combo[last] = 0
            last = cur

        if combo[BLACK] == 5:
            print(1)
            print(x - 2 + 1, y - 2 + 1)
            sys.exit(0)
        elif combo[WHITE] == 5:
            print(2)
            print(x - 2 + 1, y - 2 + 1)
            sys.exit(0)

        x += 1
        y += 1

print(0)