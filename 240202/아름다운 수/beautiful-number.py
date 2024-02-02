arr = []
count = 0
#################

def choose(n):
    global count
    if n == N+1:
        if is_beautiful():
            count += 1
        return

    arr.append(1)
    choose(n+1)
    arr.pop()

    arr.append(2)
    choose(n + 1)
    arr.pop()

    arr.append(3)
    choose(n + 1)
    arr.pop()

    arr.append(4)
    choose(n + 1)
    arr.pop()

    return

def is_beautiful():
    cur = 0
    result = True
    while cur<N:
        cur_num = arr[cur]
        if cur + cur_num > N: #만약 범위가 넘어가면
            result = False
            break
        for i in range(cur_num):
            if cur_num != arr[cur+i]: #만약 같아야 할 수가 다르다?
                result = False
                break
        if not result: break
        cur += cur_num
    return result

#################

N = int(input())

choose(1)

print(count)