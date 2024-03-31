class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# u의 다음에 v를 삽입
def insert_next(u, v):
    # v의 앞뒤 설정하기
    v.prev = u
    v.next = u.next

    # v앞의 뒤, v뒤의 앞 설정하기
    # 이때, None인지 꼭 확인하고 접근!!
    if v.next is not None:
        v.next.prev = v
    if v.prev is not None:
        v.prev.next = v


# u의 앞에 v를 삽입
def insert_prev(u, v):
    v.next = u
    v.prev = u.prev

    # insert_next와 뒷부분은 동일
    if v.next is not None:
        v.next.prev = v
    if v.prev is not None:
        v.prev.next = v

def pop(u):
    if u.next is not None:
        u.next.prev = u.prev
    if u.prev is not None:
        u.prev.next = u.next

    u.next = u.prev = None

##########################

##########################

N = int(input())
Nodes = {}
for i in range(1,N+1):
    Nodes[i] = Node(i)

Q = int(input())
for i in range(Q):
    command = input().split()
    if command[0] == '1':
        pop(Nodes[int(command[1])])
    elif command[0] == '2':
        insert_prev(Nodes[int(command[1])],Nodes[int(command[2])])
    elif command[0] == '3':
        insert_next(Nodes[int(command[1])],Nodes[int(command[2])])
    else:
        cur = int(command[1])
        if Nodes[cur].prev is not None:
            print(Nodes[cur].prev.data,end=' ')
        else:
            print(0,end=' ')
        if Nodes[cur].next is not None:
            print(Nodes[cur].next.data,end=' ')
        else:
            print(0,end=' ')
        print()

for i in range(1,N+1):
    if Nodes[i].next is not None:
        print(Nodes[i].next.data,end=' ')
    else:
        print(0,end=' ')