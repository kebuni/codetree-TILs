N, M, Q = map(int, input().split())

grid = []
winds = []

for i in range(N):
    grid.append(list(map(int, input().split())))

for i in range(Q):
    start_row, start_direct = input().split()
    start_row = int(start_row) - 1
    winds.append((start_row,start_direct))

###########################

directs = {'R': 0, 'L': 1}
visited = [False]*N

def clear_visited():
    for i in range(N):
        visited[i] = False
def wind(row, direct):
    visited[row] = True
    if direct == 1:
        temp = grid[row][M - 1]
        for i in range(M - 1, 0, -1):
            grid[row][i] = grid[row][i - 1]
        grid[row][0] = temp
    else:
        temp = grid[row][0]
        for i in range(M - 1):
            grid[row][i] = grid[row][i + 1]
        grid[row][M - 1] = temp

    if propa(row, row - 1):
        wind(row - 1, (direct + 1) % 2)

    if propa(row, row + 1):
        wind(row + 1, (direct + 1) % 2)

    return


def propa(cur, new):

    if new < 0 or new >= N:
        return False

    if visited[new] == True:
        return False

    for i in range(M):
        if grid[cur][i] == grid[new][i]:
            return True

    return False


###########################

for i in range(Q):
    wind(winds[i][0], directs[winds[i][1]])
    clear_visited()

for i in range(N):
    for elem in grid[i]:
        print(elem, end=' ')
    print()