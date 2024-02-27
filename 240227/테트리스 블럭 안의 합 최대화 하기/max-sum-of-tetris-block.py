import copy

ans = 0

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
grid2 = [[0 for i in range(N)]for j in range(M)]
grid3 = [[0 for i in range(M)]for j in range(N)]
grid4 = [[0 for i in range(N)]for j in range(M)]

block0 = [[1,1,1,1],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

block1 = [[1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0]]

block2 = [[1,1,0,0],
          [1,1,0,0],
          [0,0,0,0],
          [0,0,0,0]]

block3 = [[1,1,1,0],
          [0,0,1,0],
          [0,0,0,0],
          [0,0,0,0]]

block4 = [[1,0,0,0],
          [1,0,0,0],
          [1,1,0,0],
          [0,0,0,0]]

block5 = [[1,1,0,0],
          [0,1,1,0],
          [0,0,0,0],
          [0,0,0,0]]

block6 = [[1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,0,0,0]]

block7 = [[1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,0,0,0]]

block8 = [[1,1,1,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,0,0,0]]

blocks = [block0,block1,block2,block3,block4,block5,block6,block7,block8]

def cal_block(g,block):
    global ans

    temp_max = 0

    for x in range(len(g)):
        for y in range(len(g[0])):
            # 시작점 잡기
            sum = 0

            for dx in range(4):
                for dy in range(4):
                    if block[dx][dy]:
                        if in_range(g,x+dx,y+dy): # 블록에 해당되고 범위 안이면
                            sum += g[x+dx][y+dy]

            # 해당 시작점에서 블럭의 합 구함
            temp_max = max(temp_max,sum)

    ans = max(ans,temp_max)

    return

def in_range(g,x,y):
    return 0<=x<len(g) and 0<=y<len(g[0])

for i in range(N):
    for j in range(M):
        grid3[i][j] = grid[N-1-i][M-1-j]

for i in range(M):
    for j in range(N):
        grid2[i][j] = grid[N-1-j][i]
        grid4[i][j] = grid[j][M-1-i]

for block in blocks:
    cal_block(grid, block)
    cal_block(grid2, block)
    cal_block(grid3, block)
    cal_block(grid4, block)

print(ans)