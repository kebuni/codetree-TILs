from collections import deque
q = deque()
####################
def bfs():
    while q:
        x= q.popleft()

        if x>1 and not visited[x-1]:
            push(x-1,step[x]+1)
        
        if x<2*N and not visited[x+1]:
            push(x+1,step[x]+1)

        if x%2==0 and not visited[x//2]:
            push(x//2,step[x]+1)

        if x%3==0 and not visited[x//3]:
            push(x//3,step[x]+1)

    return

def push(x,s):
    visited[x] = 1
    step[x] = s
    #print(step)
    q.append(x)
    return

####################
N = int(input())

step = [-1 for i in range(2*N+1)]
visited = [0 for i in range(2*N+1)]

push(N,0)
bfs()

print(step[1])