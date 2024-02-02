ans =[]
#########

def choose(n):
    if n == N+1:
        for i in range(N):
            print(ans[i],end=' ')
            if i==N-1:
                print()
        return

    for i in range(K):
        ans.append(i+1)
        choose(n+1)
        ans.pop()
    
    return
    

#########

N, K = map(int,input().split())

choose(1)