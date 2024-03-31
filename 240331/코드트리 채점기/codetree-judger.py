import heapq

class Task:
    def __init__(self, _t, _p, _domain, _id):
        self.t = _t
        self.p = _p
        self.domain = _domain
        self.id = _id

    def __lt__(self, other):
        if self.p < other.p:
            return True
        elif self.p == other.p:
            return self.t < other.t
        else:
            return False

Q = int(input())
_, N, url0 = input().split()
N = int(N)
domain0, id0 = url0.split('/')
id0 = int(id0)

task_q = {}
task_q[domain0] = []
heapq.heappush(task_q[domain0],Task(0,1,domain0,id0))
judge_q = []
for i in range(1,N+1):
    heapq.heappush(judge_q,i)
history = {}
waiting_url_pool = set()
waiting_url_pool.add((domain0,id0))
judging_domain_pool = set()
judging = {}
######################################

def request_task(time,priority,url):
    # 만약 대기 중인 url 중에 해당 url이 있으면 넘어감
    domain, id = url.split('/')

    if (domain,id) in waiting_url_pool:
        return

    # task_q 넣기
    if domain not in task_q:
        task_q[domain] = []
    heapq.heappush(task_q[domain], Task(time, priority, domain, id))

    # waiting url pool 넣기
    waiting_url_pool.add((domain,id))

    return

def try_judge(time):

    INT_MAX = 98754321
    min_task = Task(INT_MAX, INT_MAX, 'notask', -1)

    # 가능한 도메인 중 최우선순위 task를 찾습니다.
    for domain in task_q:
        
        if not task_q[domain]:
            continue
        
        if available_domain(domain,time):
            temp = heapq.heappop(task_q[domain])
            if temp < min_task:
                min_task = temp
            heapq.heappush(task_q[domain],temp)

    # 가능한 task가 없으면 return합니다.
    min_p = min_task.p
    min_domain = min_task.domain
    min_id = min_task.id
    if min_id == -1:
        return
    else: # 가능한 task가 있으면
        # task_q 업데이트
        heapq.heappop(task_q[min_domain])
        # judge_q 업데이트
        new_judge = heapq.heappop(judge_q)
        # waiting pool 업데이트
        waiting_url_pool.remove((min_domain,min_id))
        # judging 업데이트
        judging[new_judge] = Task(time,min_p,min_domain,min_id)
        # judging pool 업데이트
        judging_domain_pool.add(min_domain)

    return

def available_domain(domain, time):
    if domain in judging_domain_pool:
        return False

    if domain not in history:
        return True

    start_t, end_t = history[domain]
    gap = end_t - start_t
    if time < start_t + 3*gap:
        return False

    return True

def finish_judge(time,judge_id):
    # 만약 judge_id가 채점 중이 아니면 return
    if judge_id not in judging:
        return

    # judge_id가 채점 중이었다면
    _t = judging[judge_id].t
    _p = judging[judge_id].p
    _domain = judging[judge_id].domain
    _id = judging[judge_id].id

    # history 업데이트
    history[_domain] = (_t,time)
    # judge_q 업데이트
    heapq.heappush(judge_q,judge_id)
    # judging_domin_pool 업데이트
    judging_domain_pool.remove(_domain)
    # judging 업데이트
    judging.pop(judge_id)
    return

def print_task_num():
    num = 0
    for domain in task_q:
        num += len(task_q[domain])
    print(num)
    return

def print_status(q,command):
    print(q,command,'=============================')
    print("task_q:",end=' ')
    print(task_q)
    print("url pool:", end=' ')
    print(waiting_url_pool)
    print("judging:", end=' ')
    print(judging)
    print("domain pool:", end=' ')
    print(judging_domain_pool)
    print("judge_q:", end=' ')
    print(judge_q)
    print("history:", end=' ')
    print(history)
    print()

######################################

# print_status(0,"init")

for _ in range(Q-1):
    query, *command = input().split()
    query = int(query)

    if query == 200:
        request_task(int(command[0]),int(command[1]),command[2])
    elif query == 300:
        try_judge(int(command[0]))
    elif query == 400:
        finish_judge(int(command[0]),int(command[1]))
    else:
        print_task_num()

    # print_status(query, command)