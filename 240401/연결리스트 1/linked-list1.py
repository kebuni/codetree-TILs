class Node:
    def __init__(self, s):
        self.data = s 
        self.next = None
        self.prev = None

S_init = input()
N = int(input())

################

def insert_next(u, v):
    v.prev = u
    v.next = u.next

    if v.prev is not None:
        v.prev.next = v
    if v.next is not None:
        v.next.prev = v

def insert_prev(u, v):
    v.next = u
    v.prev = u.prev

    if v.prev is not None:
        v.prev.next = v
    if v.next is not None:
        v.next.prev = v

################

cur = Node(S_init)

for i in range(N):
    command = input().split()
    if command[0] == '1':
        insert_prev(cur, Node(command[1]))
    elif command[0] == '2':
        insert_next(cur, Node(command[1]))
    elif command[0] == '3':
        if cur.prev is not None:
            cur = cur.prev
    else:
        if cur.next is not None:
            cur = cur.next

    if cur.prev is None:
        print("(Null)",end=' ')
    else:
        print(cur.prev.data,end=' ')
    
    print(cur.data,end=' ')

    if cur.next is None:
        print("(Null)",end=' ')
    else:
        print(cur.next.data,end=' ')

    print()