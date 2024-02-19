import sys

INT_MAX = sys.maxsize

MAX_R = 1000
MAX_Q = 4

# 변수 선언 및 입력:
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = INT_MAX

# x 기준 오름차순으로 정렬합니다.
points.sort()

# y = b를 먼저 설정합니다.
for b in range(0, MAX_R + 1, 2):
    # 1, 2, 3, 4 각 사분면에 
    # 들어 있는 점의 개수를 관리합니다.
    cnt = [0] * (MAX_Q + 1)

    # 먼저 x = 0일 때의
    # 1, 2, 3, 4 각 사분면에
    # 있는 점의 수를 계산합니다. 
    # 모든 점은 x = 0 보다 오른쪽에 있으므로
    # 이는 y좌표에 따라 1, 4 사분면으로 나뉘게 됩니다.
    for _, y in points:
        if y > b:
            cnt[1] += 1
        else:
            cnt[4] += 1

    # 이제 x 기준 오름차순으로 정렬된 
    # n개의 점을 보며 
    # 각 점을 순서대로 왼쪽으로 보내며
    # 1 -> 2 사분면으로
    # 4 -> 3 사분면으로 점들의 위치를 보정해줍니다.
    for i in range(n):
        # 새로운 x값이 시작되는 경우에는
        # 답을 갱신해줍니다.
        if i == 0 or points[i][0] != points[i - 1][0]:
            ans = min(ans, max(cnt))
    
        # 해당 점의 위치를 보정해줍니다.
        _, y = points[i]
        if y > b:
            cnt[1] -= 1
            cnt[2] += 1
        else:
            cnt[4] -= 1
            cnt[3] += 1

print(ans)