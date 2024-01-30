OUT_OF_GRID = -1

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(center_x, center_y):
    # Step1. next_grid 값을 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # Step2. 폭탄이 터질 위치는 0으로 채워줍니다.
    bomb_range = grid[center_x][center_y]
    
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0
	
    # Step3. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
                
    # Step4. grid로 다시 값을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# 해당 col 열에 폭탄이 터질 위치를 구합니다.
# 없다면 OUT_OF_GRID를 반환합니다.
def get_bomb_row(col):
    for row in range(n):
        if grid[row][col] != 0:
            return row
    
    return OUT_OF_GRID

        
# m번에 걸쳐 폭탄이 터집니다.
for _ in range(m):
    bomb_col = int(input()) - 1

    # 폭탄이 터지게 될 위치를 구합니다.
    bomb_row = get_bomb_row(bomb_col)

    if bomb_row == OUT_OF_GRID:
        continue

    bomb(bomb_row, bomb_col)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()