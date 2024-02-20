from collections import deque
import heapq

customers = {}
sushies_num = {}
last_sushi_time = {}
sushies = {}

###########################

def make_sushi(t,x,name):

    #if name not in customers:
    #    customers[name] = [-1,-1,-1,-1]

    if name not in sushies:
        sushies_num[name] = 0
        sushies[name] = []
        last_sushi_time[name] = -1
    #sushies[name].append([t,x,sushi_out_time(t,x,name)])

    sushi_ot = sushi_out_time(t,x,name)
    last_sushi_time[name] = max(sushi_ot,last_sushi_time[name])
    heapq.heappush(sushies[name],(sushi_ot,t,x))
    sushies_num[name] += 1

    ### 손님 나갈 시간 업데이트
    if name in customers:
        customers[name][3] = update_customer_out_time(name,customers[name][1])

    return

def new_customer(t,x,name,sushi_num):

    if name not in sushies:
        sushies[name] = []
        sushies_num[name] = 0
        last_sushi_time[name] = -1

    customers[name] = [t,x,sushi_num,-1]
    out_time = update_customer_out_time(name,x)
    customers[name][3] = out_time

    sushi_list = sushies[name].copy()
    sushies[name] = []
    for sushi in sushi_list:
        ot = sushi_out_time(t, (t+sushi[2]-sushi[1])%L, name)
        last_sushi_time[name] = max(ot, last_sushi_time[name])
        heapq.heappush(sushies[name],(ot,sushi[1],sushi[2]))

    out_time = update_customer_out_time(name, x)
    customers[name][3] = out_time

    return

def take_picture(t):

    #print(customers)

    out_list = []

    for customer in customers:
        if customers[customer][3] != -1 and customers[customer][3] <= t:
            out_list.append(customer)

    for customer in out_list:
        customers.pop(customer)
        sushies.pop(customer)
        sushies_num.pop(customer)

    print(len(customers),end=' ')

    sum = 0
    for name in sushies:
        while sushies[name]:
            if sushies[name][0][0] != -1 and sushies[name][0][0] <= t:
                #sushi_list.popleft()
                heapq.heappop(sushies[name])
            else:
                sum += len(sushies[name])
                break

    print(sum)

    return

def sushi_out_time(t,x,name):

    #손님이 없으면 영원히 존재할 것임
    if name not in customers:
        return -1

    #손님이 있다면..
    customer_location = customers[name][1]

    if customer_location > x :
        return t + customer_location - x
    elif customer_location == x :
        return t
    else:
        return t + (L + customer_location - x)

def update_customer_out_time(name,customer_location):
    global customers

    if sushies_num[name] != customers[name][2]:
        return -1

    # 먹어야 할 초밥이 다 생성 됐다는 뜻 -> 마지막 초밥으로 시간 계산
    # last_sushi = sushies[name][-1]
    # t = last_sushi[0]
    # x = last_sushi[1]
    # if customer_location > x:
    #     return t + customer_location - x
    # elif customer_location == x:
    #     return t
    # else:
    #     return t + (L + customer_location - x)
    return last_sushi_time[name]

###########################

L, Q = map(int,input().split())

for _ in range(Q):
    command = list(input().split())
    if command[0] == '100':
        t = int(command[1])
        x = int(command[2])
        name = command[3]
        make_sushi(t,x,name)
    elif command[0] == '200':
        t = int(command[1])
        x = int(command[2])
        name = command[3]
        sushi_num = int(command[4])
        new_customer(t,x,name,sushi_num)
    else:
        t = int(command[1])
        take_picture(t)

    # print("customers:",customers)
    # print("sushies_num: ",sushies_num)
    # print("sushies:",sushies)
    # print('------------------------------------')