class Query:
    def __init__(self,query_num,t,x,name,num):
        self.query_num = query_num
        self.t = t
        self.x = x
        self.name = name
        self.num = num

    def __lt__(self,other):
        if self.t < other.t:
            return True
        elif self.t == other.t:
            return self.query_num < other.query_num
        else:
            return False

def print_query_list():
    for q in query_list:
        print(q.query_num,q.t,q.x,q.name,q.num)
    print('---------------')

ans_sushi_num = 0
ans_customer_num = 0

customer_info = {}
customer_exit_time = {}

L, Q = map(int,input().split())
query_list = []
additional_query_list = []
for i in range(Q):
    command = list(input().split())
    if command[0] == '100':
        t = int(command[1])
        x = int(command[2])
        query_list.append(Query(100,t,x,command[3],-1))
    elif command[0] == '200':
        t = int(command[1])
        x = int(command[2])
        n = int(command[4])
        query_list.append(Query(200,t,x,command[3],n))
        customer_info[command[3]] = [t,x,n,0]
        customer_exit_time[command[3]] = -1
    else:
        t = int(command[1])
        query_list.append(Query(300, t, -1, "", -1))

# print_query_list()

for q in query_list:
    if q.query_num == 100:
        sushi_t = q.t
        sushi_x = q.x
        customer_t = customer_info[q.name][0]
        customer_x = customer_info[q.name][1]
        out_time = -1
        # 초밥이 먼저 나왔다면
        if sushi_t < customer_t:
            after_sushi_x = (sushi_x + (customer_t - sushi_t)) % L
            out_time = customer_t + ((customer_x - after_sushi_x + L) % L)
        # 초밥이 나중에 나왔다면
        else:
            out_time = sushi_t + ((customer_x - sushi_x + L) % L)
        # 초밥이 사라지는 시간을 계산해서 111 쿼리를 추가합니다
        additional_query_list.append(Query(111,out_time,-1,"",-1))
        # customer가 먹은 초밥 개수를 업데이트합니다.
        customer_info[q.name][3] += 1
        customer_exit_time[q.name] = max(customer_exit_time[q.name], out_time)
        # 만약 customer가 모든 초밥을 먹었다면 222 쿼리를 추가합니다.

for name, exit_time in customer_exit_time.items():
    additional_query_list.append(Query(222,exit_time,-1,name,-1))

# 새로운 쿼리를 추가해서 정렬합니다.
query_list += additional_query_list
query_list.sort()
# print_query_list()
# print(customer_exit_time)

# 쿼리마다 ans를 더하거나 빼고 300 쿼리에선 프린트합니다.
for q in query_list:
    if q.query_num == 100:
        ans_sushi_num += 1
    elif q.query_num == 111:
        ans_sushi_num -= 1
    elif q.query_num == 200:
        ans_customer_num += 1
    elif q.query_num == 222:
        ans_customer_num -= 1
    else:
        print(ans_customer_num,ans_sushi_num)