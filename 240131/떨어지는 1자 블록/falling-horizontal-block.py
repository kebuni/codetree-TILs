grid = []
highest_floor = 99999

################

def find_floor(col):
    for i in range(n):
        if grid[i][col] == 0:
            floor = i
        else:
            break
    return floor

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end=' ')
        print()

################

n, m, k = map(int,input().split())
k = k - 1

for _ in range(n):
    grid.append(list(map(int,input().split())))

for col in range(k,k+m):
    highest_floor = min(highest_floor, find_floor(col))

for col in range(k,k+m):
    grid[highest_floor][col] = 1

print_grid()