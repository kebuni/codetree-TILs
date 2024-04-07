class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def connect(u,v):
    if u:
        u.next = v
    if v:
        v.prev = u

def make_line(start,num):
    # start 부터 num 명을 줄세웁니다.
    cur = None
    for i in range(num):
        new_node = Node(start+i)
        node[start+i] = new_node
        if i == 0:
            cur = new_node
            continue
        connect(cur,new_node)
        cur = new_node

    return

def push_line_next(u,s,e):
    connect(e,u.next)
    connect(u,s)
    return

def push_line_prev(u,s,e):
    connect(u.prev,s)
    connect(e,u)
    return

def print_ans(u):
    if u.prev and u.next:
        print(u.prev.data,u.next.data)
    else:
        print(-1)
    return

#############################

node = {}
node[1] = Node(1)
next_num = 2

Q = int(input())
for i in range(Q):
    command = list(input().split())
    if command[0] == '1':
        a = int(command[1])
        b = int(command[2])
        make_line(next_num, b)
        push_line_next(node[a],node[next_num],node[next_num+b-1])
        next_num += b
    elif command[0] == '2':
        a = int(command[1])
        b = int(command[2])
        make_line(next_num, b)
        push_line_prev(node[a],node[next_num],node[next_num+b-1])
        next_num += b
    else:
        a = int(command[1])
        print_ans(node[a])