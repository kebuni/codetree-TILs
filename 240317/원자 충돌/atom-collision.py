dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]
direct_to_arrow = ['↑','↗','→','↘','↓','↙','←','↖']

N, M, K = map(int,input().split())
grid = [[[] for i in range(N)] for j in range(N)]
next_grid = [[[] for i in range(N)] for j in range(N)]
for _ in range(M):
    x, y, m, s, d = map(int,input().split())
    grid[x-1][y-1].append((m,s,d))

PADDING = N*300

###################################################

def move_all_atoms():
    for x in range(N):
        for y in range(N):
            for atom in grid[x][y]:
                move(x,y,atom)
    return

def move(x,y,atom):
    m, s, d = atom
    nx = (x + s * dxs[d] + PADDING) % N
    ny = (y + s * dys[d] + PADDING) % N
    next_grid[nx][ny].append((m,s,d))
    return

def split_all_atoms():
    #next에서 해야 함
    for x in range(N):
        for y in range(N):
            if len(next_grid[x][y]) > 1:
                split(x,y)
    return

def split(x,y):
    atom_num = len(next_grid[x][y])
    mass_sum, speed_sum = 0, 0
    orthogonal_sum = [0, 0]
    orthogonal = [0,2,4,6]
    diagonal = [1,3,5,7]

    for m, s, d in next_grid[x][y]:
        mass_sum += m
        speed_sum += s
        orthogonal_sum[d%2] += 1

    next_grid[x][y].clear()
    if orthogonal_sum[0] == 0 or orthogonal_sum[1] == 0:
        for i in range(4):
            next_grid[x][y].append((mass_sum//5, speed_sum//atom_num, orthogonal[i]))
    else:
        for i in range(4):
            next_grid[x][y].append((mass_sum//5, speed_sum//atom_num, diagonal[i]))

    return

def sum_of_mass():
    sum = 0
    for x in range(N):
        for y in range(N):
            for m, _, _ in grid[x][y]:
                sum += m
    return sum

def copy_grid():
    for x in range(N):
        for y in range(N):
            grid[x][y].clear()
            for elem in next_grid[x][y]:
                if elem[0]:
                    grid[x][y].append(elem)
            next_grid[x][y].clear()
    return

def print_grid():
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()

def print_next_grid():
    for x in range(N):
        for y in range(N):
            print(next_grid[x][y], end=' ')
        print()
    print()

###################################################

for _ in range(K):
    #print("=============")
    move_all_atoms()
    #print_next_grid()

    split_all_atoms()
    #print_next_grid()

    copy_grid()
    #print_grid()

print(sum_of_mass())