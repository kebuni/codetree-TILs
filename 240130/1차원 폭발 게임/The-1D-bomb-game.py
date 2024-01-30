bombs = []

#########

def simulate():

    global bombs

    while(1):
        escape = True
        start = 0
        end = 0
        cnt = 1
        prev = bombs[0]
        for i in range(1,N):
            if bombs[i] == 0: #이제 터지는 건 다했고 떨어지자
                break
            if prev == bombs[i]: # 콤보!
                end += 1
                cnt += 1
            else: # 콤보가 끝났다면 이제 터질지 평가하자
                if cnt >= M:
                    for k in range(start,end+1):
                        bombs[k] = 0
                        escape = False

                prev = bombs[i]
                start = i
                end = i
                cnt = 1

        if cnt >= M:
            for k in range(start,end+1):
                bombs[k] = 0
                escape = False
        
        fall()

        if escape:
            break

def fall():
    global bombs

    temp = [0] * N
    cnt = 0
    for elem in bombs:
        if elem:
            temp[cnt] = elem
            cnt += 1
    
    for i in range(N):
        bombs[i] = temp[i]

def print_bombs():
    cnt = 0
    for elem in bombs:
        if not elem:
            break
        cnt += 1

    print(cnt)
    for i in range(cnt):
        print(bombs[i])

#########

N, M = map(int,input().split())

for _ in range(N):
    bombs.append(int(input()))

simulate()

print_bombs()