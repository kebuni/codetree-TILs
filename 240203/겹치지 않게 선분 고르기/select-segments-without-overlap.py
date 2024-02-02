sunbun = []
selected = []
ans = 0
#########################

def select(n): #n번째 이후로 검색해서 추가

    # print("here is ...",n)
    global ans
    if n==N:
        ans = max(ans,len(selected))
        # print(selected)
        return

    selected.append(sunbun[n])

    start, end = sunbun[n]
    next_idx = N
    for i in range(n+1,N):
        temp, _ = sunbun[i]
        if temp > end: #만약 다음 선분 시작점이 현재 end보다 크다면,
            next_idx = i
            break
    for i in range(next_idx,N+1):
        select(i)

    selected.pop()
    return

#########################

N = int(input())

for _ in range(N):
    sunbun.append(tuple(map(int,input().split())))

sunbun.sort()
# print(sunbun)

for i in range(N+1):
    select(i)

print(ans)