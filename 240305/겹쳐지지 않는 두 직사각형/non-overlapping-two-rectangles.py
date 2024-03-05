import sys
N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

ans = - sys.maxsize

def get_sum(x1,y1,x2,y2):
    sum = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            sum += grid[i][j]
    return sum

def valid(x1,y1,x2,y2,x3,y3,x4,y4):
    board = [[0 for i in range(M)] for j in range(N)]

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j] += 1
    
    for i in range(x3,x4+1):
        for j in range(y3,y4+1):
            if board[i][j] == 1:
                return False
    
    return True


for x1 in range(N):
    for y1 in range(M):
        for x2 in range(x1,N):
            for y2 in range(y1,M):

                sum1 = get_sum(x1,y1,x2,y2)

                for x3 in range(N):
                    for y3 in range(M):
                        for x4 in range(x3,N):
                            for y4 in range(y3,M):
                                
                                if valid(x1,y1,x2,y2,x3,y3,x4,y4):
                                    sum2 = get_sum(x3,y3,x4,y4)
                                    ans = max(ans,sum1+sum2)

print(ans)