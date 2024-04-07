class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def connect(s,e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s
    return

def insert_next(u,v):
    connect(v,u.next)
    connect(u,v)
    return

def insert_prev(u,v):
    connect(u.prev,v)
    connect(v,u)
    return

def pop(u):
    connect(u.prev,u.next)
    u.prev = u.next = None
    return

#############################

N, K = map(int,input().split())
head = [None for i in range(K+1)]
tail = [None for i in range(K+1)]

head[1] = Node(1)
cur = head[1]
for i in range(2,N+1):
    new_node = Node(i)
    insert_next(cur, new_node)
    cur = new_node
    if i == N:
        tail[1] = new_node

#############################
def print_head():
    for i in range(1, K + 1):
        if head[i] is not None:
            print(head[i].data, end=' ')
        else:
            print(-1, end=' ')
    print()
    return

def print_tail():
    for i in range(1, K + 1):
        if tail[i] is not None:
            print(tail[i].data, end=' ')
        else:
            print(-1, end=' ')
    print()
    return

def pop_front(i):
    if head[i] is None:
        return None

    _head = head[i]
    # 노드가 하나일 경우
    if _head.next is None:
        head[i] = None
        tail[i] = None
    # 노드가 여러 개일 경우
    else:
        head[i] = _head.next
        _head.next = None
        head[i].prev = None

    return _head

def pop_back(i):
    if tail[i] is None:
        return None

    _tail = tail[i]
    if tail[i].prev is None:
        head[i] = None
        tail[i] = None
    else:
        tail[i] = _tail.prev
        _tail.prev = None
        tail[i].next = None

    return _tail

def push_front(i,u):
    if head[i] is None:
        head[i] = u
        tail[i] = u
    else:
        connect(u,head[i])
        head[i] = u
    return

def push_back(i,u):
    if tail[i] is None:
        head[i] = u
        tail[i] = u
    else:
        connect(tail[i],u)
        tail[i] = u
    return

def remove_all_and_push_front(i,j):
    if i == j or head[i] == None:
        return

    # j가 비었다면
    if head[j] is None:
        head[j] = head[i]
        tail[j] = tail[i]
    else:
        connect(tail[i],head[j])
        head[j] = head[i]

    head[i] = tail[i] = None
    return

def remove_all_and_push_back(i,j):
    if i == j or head[i] == None:
        return

    if head[j] is None:
        head[j] = head[i]
        tail[j] = tail[i]
    else:
        connect(tail[j],head[i])
        tail[j] = tail[i]

    head[i] = tail[i] = None
    return

def print_ans():
    for i in range(1,K+1):
        book_list = []
        cur = head[i]
        while cur is not None:
            book_list.append(cur.data)
            cur = cur.next

        print(len(book_list),end=' ')
        for elem in book_list:
            print(elem,end=' ')
        print()
    return

#############################

Q = int(input())
query = [tuple(map(int,input().split())) for i in range(Q)]
for q_num, s_num, d_num in query:
    if q_num == 1:
        temp = pop_front(s_num)
        if temp is not None:
            push_back(d_num,temp)
    elif q_num == 2:
        temp = pop_back(s_num)
        if temp is not None:
            push_front(d_num, temp)
    elif q_num == 3:
        remove_all_and_push_front(s_num, d_num)
    else:
        remove_all_and_push_back(s_num, d_num)

    # print("query",q_num,s_num,d_num)
    # print_ans()
    # print("head:")
    # print_head()
    # print("tail:")
    # print_tail()

print_ans()