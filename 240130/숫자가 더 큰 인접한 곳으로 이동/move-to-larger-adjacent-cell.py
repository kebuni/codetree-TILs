grid = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
visited = []


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(x, y):
    global visited
    can_move = False

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx,ny):
            if grid[nx][ny] > grid[x][y]:
                can_move = True
                visited.append(grid[nx][ny])
                break

    return nx, ny, can_move


n, r, c = map(int, input().split())
for i in range(n):
    grid.append(list(map(int, input().split())))

x = r - 1
y = c - 1

visited.append(grid[x][y])

while True:
    x, y, can_move = move(x, y)
    if can_move == False:
        break

for elem in visited:
    print(elem, end=' ')