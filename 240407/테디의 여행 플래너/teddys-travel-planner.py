class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def connect(u,v):
    if u is not None:
        u.next = v
    if v is not None:
        v.prev = u
    return

def insert_next(u,v):
    # u의 다음에 v를 삽입
    connect(v,u.next)
    connect(u,v)
    return

def pop(u):
    connect(u.prev,u.next)
    u.prev = u.next = None
    return

##########################

N, Q = map(int,input().split())
cities = list(input().split())
first_city = cities[0]
head = Node(first_city)
tail = head
for i in range(1,N):
    new_node = Node(cities[i])
    insert_next(tail,new_node)
    tail = new_node

connect(tail,head)

cur = head
for _ in range(Q):
    command = list(input().split())
    if command[0] == '1':
        cur = cur.next
    elif command[0] == '2':
        cur = cur.prev
    elif command[0] == '3':
        pop(cur.next)
    else:
        insert_next(cur,Node(command[1]))

    #print(command)
    #print("cur",cur.data)

    if cur.prev is None or cur.next is None:
        print(-1)
    elif cur.prev.data == cur.next.data:
        print(-1)
    else:
        print(cur.prev.data,cur.next.data)