import heapq

# 입력:
n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

# 변수 선언
pq = []

for x in arr:
    if x != 0:
        # x가 자연수라면
        # priority queue에 x를 넣어줍니다.
        heapq.heappush(pq, -x)
    
    else:
        # x가 0이라면
        # 최댓값을 찾아 출력한 뒤 제거합니다.
        if not pq:
            print(0)
        else:
            print(-heapq.heappop(pq))