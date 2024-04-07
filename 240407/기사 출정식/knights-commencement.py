class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def connect(s,e):
    if s:
        s.next = e
    if e:
        e.prev = s 

def pop(u):
    connect(u.prev,u.next)
    u.prev = u.next = None

N, M = map(int,input().split())
arr = list(map(int,input().split()))
head = None
tail = None
node = {}
for i, elem in enumerate(arr):
    new_node = Node(elem)
    node[elem] = new_node
    if i == 0:
        head = new_node
        tail = new_node
        continue
    connect(tail,new_node)
    tail = new_node

connect(tail,head)
for i in range(M):
    query = int(input())
    print(node[query].next.data,end=' ')
    print(node[query].prev.data)
    
    pop(node[query])