import heapq

q = []

N = int(input())

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        A = int(command[1])
        heapq.heappush(q,-A)
    elif command[0] == 'pop':
        B = heapq.heappop(q)
        print(-B)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    else:
        print(-q[0])