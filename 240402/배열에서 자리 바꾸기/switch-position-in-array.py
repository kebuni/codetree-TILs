# 한 노드를 나타내는 구조체입니다.
class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

MAX_N = 250000
nodes = [None] * (MAX_N + 1)

# 두 노드를 연결해줍니다.
def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

# 부분 배열의 위치를 바꿔줍니다.
def swapSubarray(a, b, c, d):
    # 연결된 이후 각각 a의 이전노드, b의 이후노드, c의 이전노드, d의 이후노드가
    # 무엇인지 기록합니다.
    after_prevA = c.prev
    after_nextB = d.next

    after_prevC = a.prev
    after_nextD = b.next

    # b와 c가 붙어있는 경우 예외 처리를 해줍니다.
    if b.next == c:
        after_prevA = d
        after_nextD = a
    # d와 a가 붙어있는 경우 예외 처리를 해줍니다.
    if d.next == a:
        after_nextB = c
        after_prevC = b

    # 각각의 노드를 연결합니다.
    connect(after_prevA, a)
    connect(b, after_nextB)

    connect(after_prevC, c)
    connect(d, after_nextD)


n = int(input())

# N개의 노드를 생성합니다.
for i in range(1, n + 1):
    nodes[i] = Node(i)

# 1부터 N번 까지의 노드를 차례로 연결해줍니다.
for i in range(1, n):
    connect(nodes[i], nodes[i + 1])

q = int(input())

# 연산을 진행합니다.
for _ in range(q):
    a, b, c, d = map(int, input().split())
    swapSubarray(nodes[a], nodes[b], nodes[c], nodes[d])

# 연산이 끝나고 제일 앞에 있는 노드를 찾습니다.
cur = nodes[1]
while cur.prev:
    cur = cur.prev

# 해당 노드부터 끝까지 출력을 합니다.
while cur:
    print(cur.id, end=" ")
    cur = cur.next