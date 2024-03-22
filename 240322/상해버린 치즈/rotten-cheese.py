T = 100
N, M, D, S = map(int,input().split())
sick_list = []
cadidate = set([m for m in range(1,M+1)])
new_cadidate = set()

table = [[[] for t in range(T+1)] for n in range(N+1)]

for i in range(D):
    p, m, t = map(int,input().split())
    table[p][t].append(m)

for i in range(S):
    p, t = map(int,input().split())
    sick_list.append((p,t))

for p, t in sick_list:
    new_cadidate = set()
    # 이번 아픈 사람 p의 기록을 볼 겁니다
    for i in range(1,t):
        for c in table[p][i]:
            if c in cadidate:
                new_cadidate.add(c)
    cadidate = new_cadidate

# 상할 수 있는 치즈 후보를 추렸습니다 이제 먹은 사람에게 약을 줍니다
need_medicine = [False for i in range(N+1)]
for p in range(1,N+1):
    for t in range(1,T+1):
        for c in table[p][t]:
            if c in cadidate:
                need_medicine[p] = True

ans = 0
for i in range(1,N+1):
    if need_medicine[i]:
        ans += 1

print(ans)