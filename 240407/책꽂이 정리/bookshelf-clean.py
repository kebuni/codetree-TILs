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

def query1(s_num,d_num):
    s_head = head[s_num]
    if s_head is None:
        return
    s_head_next = s_head.next
    pop(s_head)
    head[s_num] = s_head_next
    d_tail = tail[d_num]
    connect(d_tail,s_head)
    tail[d_num] = s_head
    if head[d_num] == None:
        head[d_num] = tail[d_num]
    return

def query2(s_num,d_num):
    s_tail = tail[s_num]
    if s_tail is None:
        return
    s_tail_prev = s_tail.prev
    pop(s_tail)
    tail[s_num] = s_tail_prev
    d_head = head[d_num]
    connect(s_tail,d_head)
    head[d_num] = s_tail
    if tail[d_num] == None:
        tail[d_num] = head[d_num]
    return

def query3(s_num,d_num):
    s_head = head[s_num]
    if s_head is None:
        return
    s_tail = tail[s_num]
    if s_tail is None:
        return

    head[s_num] = None
    tail[s_num] = None

    d_head = head[d_num]
    connect(s_tail,d_head)
    head[d_num] = s_head
    if tail[d_num] == None:
        tail[d_num] = head[d_num]
    return

def query4(s_num,d_num):
    s_head = head[s_num]
    if s_head is None:
        return
    s_tail = tail[s_num]
    if s_tail is None:
        return

    head[s_num] = None
    tail[s_num] = None

    d_tail = tail[d_num]
    connect(d_tail, s_head)
    tail[d_num] = s_tail

    if head[d_num] == None:
        head[d_num] = tail[d_num]

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
        query1(s_num, d_num)
    elif q_num == 2:
        query2(s_num, d_num)
    elif q_num == 3:
        query3(s_num, d_num)
    else:
        query4(s_num, d_num)

    # print("query",q_num,s_num,d_num)
    # print_ans()
    # print("head:")
    # print_head()
    # print("tail:")
    # print_tail()

print_ans()