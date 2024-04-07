class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def connect(u, v):
    if u:
        u.next = v
    if v:
        v.prev = u

def insert_prev(u, v):
    connect(u.prev, v)
    connect(v, u)

def pop(u):
    connect(u.prev,u.next)
    u.prev = u.next = None

def pop_all_and_insert_prev(u, s, e):
    connect(s.prev, e.next)
    s.prev = e.next = None
    connect(u.prev, s)
    connect(e, u)


def print_status():
    for i in range(M):
        print("[line", i, "]", end=' ')
        print("line:", end=' ')
        cur = nodes[-i]
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()
    return

def print_ans():
    for i in range(M):
        head = nodes[-i]
        if head.next == None:
            print(-1)
        else:
            cur = head.next
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next
            print()
    return

###########################

N, M, Q = map(int, input().split())
nodes = {}
arr = list(input().split())
for line_num in range(M):
    nodes[-line_num] = Node(-line_num)
    cur = nodes[-line_num]
    for x in range(N//M):
        name = arr[N//M*line_num + x]
        new_node = Node(name)
        nodes[name] = new_node
        connect(cur,new_node)
        cur = cur.next

for i in range(Q):
    command = list(input().split())
    if command[0] == '1':
        a = command[1]
        b = command[2]
        pop(nodes[a])
        insert_prev(nodes[b],nodes[a])
    elif command[0] == '2':
        a = command[1]
        pop(nodes[a])
    else:
        a = command[1]
        b = command[2]
        c = command[3]
        pop_all_and_insert_prev(nodes[c],nodes[a],nodes[b])

print_ans()