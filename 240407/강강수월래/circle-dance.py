import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

def connect(u,v):
    if u:
        u.next = v
    if v:
        v.prev = u

def merge(u,v):
    connect(v.prev,u.next)
    connect(u,v)
    return

def split(u,v):

    # 예외처리
    if u == v:
        pop(u)
        return

    if u.next == v:
        connect(u.prev, v)
        pop(u)
        return

    if v.next == u:
        pop(u)
        pop(v)
        return

    u_prev = u.prev
    v_prev = v.prev

    connect(v_prev,u)
    connect(u_prev,v)
    return

def pop(u):
    connect(u.prev,u.next)
    u.prev = u.next = u
    return

def print_ans(u):
    min_num = u.data
    cur = u.prev
    while cur != u:
        min_num = min(min_num,cur.data)
        cur = cur.prev

    end = node[min_num]
    print(end.data,end=' ')
    cur = end.prev
    while cur != end:
        print(cur.data,end=' ')
        cur = cur.prev
    print()
    return

def print_node_status():
    for key in node:
        print("[node",key,"]")
        if node[key].prev:
            print("prev:",node[key].prev.data,end=' ')
        else:
            print("prev: None",end=' ')
        if node[key].next:
            print("next:",node[key].next.data)
        else:
            print("next: None")

#####################################

N, M, Q = map(int,input().split())
node = {}
for i in range(M):
    size, *arr = list(map(int,input().split()))
    head = None
    tail = None
    for j in range(size):
        new_node = Node(arr[j])
        node[arr[j]] = new_node
        if j == 0:
            head = new_node
            tail = new_node
            continue
        connect(tail,new_node)
        tail = new_node
    connect(tail,head)

# print("initialized ================")
# print_node_status()

for i in range(Q):
    q_num, *command = list(map(int,input().split()))
    if q_num == 1:
        merge(node[command[0]],node[command[1]])
    elif q_num == 2:
        split(node[command[0]],node[command[1]])
    else:
        print_ans(node[command[0]])

    # print("query :",q_num,command,'================')
    # print_node_status()