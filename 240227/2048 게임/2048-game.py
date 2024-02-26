NUM_MOVES = 5
NONE = -1

# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

move_dirs = [0 for _ in range(NUM_MOVES)]

ans = 0


def get_max_block_num():
    return max([
        grid[i][j]
        for i in range(n)
        for j in range(n)
    ])


# grid를 시계방향으로 90' 회전시킵니다.
def rotate():
    # next_grid를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # 90' 회전합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n - j - 1][i]
    
    # next_grid를 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# 아래로 숫자들을 떨어뜨립니다.
def drop():
    # next_grid를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # 아래 방향으로 떨어뜨립니다.
    for j in range(n):
        # 같은 숫자끼리 단 한번만
        # 합치기 위해 떨어뜨리기 전에
        # 숫자 하나를 keep해줍니다.
        keep_num, next_row = NONE, n - 1
        
        for i in range(n - 1, -1, -1):
            if not grid[i][j]:
                continue
            
            # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
            if keep_num == NONE:
                keep_num = grid[i][j];
            
            # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
            # 하나로 합쳐주고, keep 값을 비워줍니다.
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num * 2
                keep_num = NONE
                
                next_row -= 1
            
            # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
            # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                
                next_row -= 1
        
        # 전부 다 진행했는데도 keep 값이 남아있다면
        # 실제로 한번 떨어뜨려줍니다.
        if keep_num != NONE:
            next_grid[next_row][j] = keep_num
            next_row -= 1
    
    # next_grid를 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# move_dir 방향으로 기울이는 것을 진행합니다.
# 회전을 규칙적으로 하기 위해
# 아래, 오른쪽, 위, 왼쪽 순으로 dx, dy 순서를 가져갑니다.
def tilt(move_dir):
    # Step 1.
    # move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
    # 항상 아래로만 숫자들을 떨어뜨리면 되게끔 합니다.
    for _ in range(move_dir):
        rotate()

    # Step 2.
    # 아래 방향으로 떨어뜨립니다.
    drop()
    
    # Step 3.
    # 4 - move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
    # 처음 상태로 돌아오게 합니다. (총 360' 회전)
    for _ in range(4 - move_dir):
        rotate()


def simulate():
    global ans
    
    # 시뮬레이션 전 상황을 저장해놓습니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]
    
    # 각 방향으로 기울이는 것을 진행합니다.
    for move_dir in move_dirs:
        tilt(move_dir)
    
    # 답을 갱신합니다.
    ans = max(ans, get_max_block_num())
    
    # grid를 시뮬레이션 전 상황으로 되돌립니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def search_max_num(cnt):
    # 5번 이동할 방향을 정했다면
    # 직접 시뮬레이션을 진행합니다.
    if cnt == NUM_MOVES:
        simulate()
        return

    # 4 방향 중 이동할 방향을 선택합니다.
    for i in range(4):
        move_dirs[cnt] = i
        search_max_num(cnt + 1)


search_max_num(0)
print(ans)