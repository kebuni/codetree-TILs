selected_num = []
arr = []

######################

def choose_digit(n,cnt):
    global arr, selected_num
    if n == N+1:
        if cnt == M:
            arr.append(selected_num.copy())
        return

    choose_digit(n+1,cnt)
    selected_num.append(n)
    choose_digit(n+1,cnt+1)
    selected_num.pop()
    return

######################

N, M = map(int,input().split())

choose_digit(1,0)

arr.sort()

for elem in arr:
    for e in elem:
        print(e,end=' ')
    print()