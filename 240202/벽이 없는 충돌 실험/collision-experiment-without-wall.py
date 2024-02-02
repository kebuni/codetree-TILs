# 변수 선언 및 입력
t = int(input())
n = 0
marbles = []
collisions = []
disappear = []

last_collision_time = -1

# 3 - move_dir 방향이 move_dir 방향과 정 반대가 되도록
# move_dir에 따른 dx, dy 값을 적절하게 정의합니다.
# 후에 두 구슬의 방향이 서로 정 반대인지 쉽게 판단하기 위함입니다. 
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}


# 구슬을 무게를 내림차순으로 정렬합니다.
# 무게가 동일할 경우 숫자를 내림차순으로 정렬하여
# 정렬 이후 더 앞선 구슬들이
# 충돌시에 항상 더 영향력을 가질 수 있도록 합니다.
def cmp(marble):
    (_, _, weight, _, num) = marble
    return (-weight, -num)


# 해당 구슬의 k초 후의 위치를 계산하여 반환합니다.
def move(marble, k):
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    
    (x, y, _, move_dir, _) = marble
    nx, ny = x + dxs[move_dir] * k, y + dys[move_dir] * k
    return (nx, ny)


# 두 구슬만 좌표 평면 위에 존재한다 했을 때
# 충돌이 일어난다면 언제 일어나는지 그 시간을 반환합니다.
# 만약 충돌이 일어나지 않는다면 -1을 반환합니다.
def collision_occur_time(marble1, marble2):
    x1, y1, _, dir1, _ = marble1
    x2, y2, _, dir2, _ = marble2

    # Case1 : 두 구슬의 방향이 같은 경우에는 절대 충돌하지 않습니다.
    if dir1 == dir2:
        return -1

    # Case2 : 두 구슬의 방향이 반대인 경우에는 
    #         x, y 값 중 하나가 일치해야 하고
    #         두 구슬의 거리를 반으로 나눈 값 만큼
    #         두 구슬을 각각의 방향으로 움직였을 때 
    #         서로 같은 위치로 도달해야 충돌한다고 볼 수 있습니다. 
    if dir1 == 3 - dir2:
        # x, y 둘 다 일치하지 않으면 불가합니다.
        if x1 != x2 and y1 != y2:
            return -1
        
        # x, y 둘 중에 하나가 일치한다면 
        # 처음에 모든 좌표를 다 2배씩 해줬기 때문에 
        # dist는 짝수임을 보장할 수 있습니다. 
        dist = abs(x1 - x2) if x1 != x2 else abs(y1 - y2)
        half = dist // 2
        
        if move(marble1, half) == move(marble2, half):
            return half
        else:
            return -1

    # Case3 : 두 방향이 서로 나란히 있지 않은 경우에는
    #         두 구슬의 x좌표, y좌표의 차이가 정확히 일치해야 하며
    #         두 구슬의 각각의 방향으로 그 거리의 차이 만큼씩 움직였을 때
    #         서로 같은 위치로 도달해야 충돌한다고 볼 수 있습니다. 

    x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
    
    if x_dist == y_dist and move(marble1, x_dist) == move(marble2, x_dist):
        return x_dist
    else:
        return -1


# 모든 구슬쌍에 대해 충돌이 일어나는지 확인하고
# 발생 가능한 충돌들에 대해 시간순으로 정렬해줍니다.
def arrange_collisions():
    marble_cnt = len(marbles)
    for i in range(n):
        for j in range(i + 1, n):
            time = collision_occur_time(marbles[i], marbles[j])
            if time != -1:
                collisions.append((time, i, j))
    
    # tuple은 기본적으로 앞의 원소부터 오름차순으로 정렬하므로
    # 다음과 같이 정렬시 시간순으로 오름차순으로 정렬됨을 보장할 수 있습니다.
    collisions.sort()


# 시간에 따라 충돌 단위로 시뮬레이션을 진행합니다.
def simulate():
    global last_collision_time
    
    for collision_time, index1, index2 in collisions:
        # 두 구슬 중 하나라도 이미 이전의 충돌로 인해 소멸되어 버렸다면
        # 두 구슬은 실제로 충돌이 일어날 수 없었다는 의미이므로
        # 패스합니다.
        if disappear[index1] or disappear[index2]:
            continue
        
        # 처음에 구슬의 목록을 (무게 순, 번호가 더 큰 순)으로
        # 정렬해놨기 때문에 index1 < index2인 경우 
        # 항상 index1이 더 영향력이 크기 때문에 살아남게 되고
        # index2는 소멸하게 됩니다.
        disappear[index2] = True
        last_collision_time = collision_time


for _ in range(t):
    # 입력
    n = int(input())
    
    # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
    marbles = []
    collisions = []
    last_collision_time = -1
    
    disappear = [
        0 for _ in range(n + 1)
    ]
    
    for i in range(1, n + 1):
        x, y, weight, d = tuple(input().split())
        x, y, weight = int(x), int(y), int(weight)
        
        # 구슬이 움직이는 도중에 충돌하는 문제를 깔끔하게 처리하기 위해
        # 좌표를 2배로 불려 1초에 한칸 씩 이동하는 문제로 바꿉니다.
        # 이렇게 문제가 바뀌면 따로 구슬이 움직이는 도중 충돌하는 경우를 생각하지
        # 않아도 됩니다.
        x, y = x * 2, y * 2
        
        marbles.append((x, y, weight, mapper[d], i))
    
    # 충돌시 영향력이 더 높은 구슬이 앞으로 오도록 정렬합니다.
    # 영향력이 더 높다 함은 무게가 더 크거나, 무게가 같더라도 번호가 더 커
    # 충돌시 살아남게 되는 구슬을 의미합니다.
    marbles.sort(key = cmp)
    
    # 모든 구슬쌍에 대해 충돌이 일어나는 경우를 구해
    # 시간순으로 정리해줍니다.
    arrange_collisions()
    
    # 시간에 따라 충돌 단위로 시뮬레이션을 진행합니다.
    simulate()
    
    # 출력
    print(last_collision_time)