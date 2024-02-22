class Query:
    def __init__(self,cmd,t,x,name,n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

querys = []
exit_time = {}
sushi_querys = []
customer_querys = {}

L, Q = map(int,input().split())

for _ in range(Q):
    command = input().split()
    cmd, t, x, name, n = int(command[0]), -1, -1, -1, -1

    if cmd == 100:
        t = int(command[1])
        x = int(command[2])
        name = command[3]
        sushi_querys.append(Query(cmd,t,x,name,n))
    elif cmd == 200:
        t = int(command[1])
        x = int(command[2])
        name = command[3]
        n = int(command[4])
        customer_querys[name] = Query(cmd,t,x,name,n)
        exit_time[name] = 0
    else:
        t = int(command[1])

    querys.append(Query(cmd,t,x,name,n))

# 초밥이 사라지는 쿼리 추가
for sushi in sushi_querys:
    arrival_time = customer_querys[sushi.name].t
    customer_x = customer_querys[sushi.name].x
    # 초밥이 먼저 나옴 -> 손님이 들어올 당시 초밥의 위치 계산 해야 함
    sushi_exit_time = 0
    if sushi.t <= arrival_time:
        sushi_x = (sushi.x + (arrival_time - sushi.t)) % L
        sushi_exit_time = arrival_time + (customer_x - sushi_x + L) % L
    else: # 초밥이 늦게 손님보다 늦게 나옴 -> 바로 계산 가능
        sushi_exit_time = sushi.t + (customer_x - sushi.x + L) % L

    exit_time[sushi.name] = max(exit_time[sushi.name] , sushi_exit_time)
    querys.append(Query(111, sushi_exit_time, -1, sushi.name, -1))

# 손님이 나가는 쿼리 추가
for name in exit_time:
    t = exit_time[name]
    querys.append(Query(222, t, -1, name, -1))

# 쿼리 정렬
querys.sort(key=lambda x:(x.t,x.cmd))

# for q in querys:
#     print(q.cmd, q.name, q.t, q.x, q.n)

sushi_num = 0
customer_num = 0
for q in querys:
    if q.cmd == 100:
        sushi_num += 1
    elif q.cmd == 111:
        sushi_num -= 1
    elif q.cmd == 200:
        customer_num += 1
    elif q.cmd == 222:
        customer_num -= 1
    else:
        print(customer_num, sushi_num)