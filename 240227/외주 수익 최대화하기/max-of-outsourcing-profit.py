N = int(input())

ans = 0

work = [tuple(map(int,input().split())) for _ in range(N)]

def choose(n,finish,profit_sum):
    global ans
    if n == N:
        ans = max(ans,profit_sum)
        return

    t, p = work[n]
    if n >= finish and n+t <= N:
        choose(n+1,n+t,profit_sum+p)
    choose(n+1,finish,profit_sum)

    return

choose(0,0,0)

print(ans)