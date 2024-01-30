# 입력값 1부터 조심

arr = []

############

def process(s,e):

    global arr

    for i in range(s,e+1):
        arr[i] = 0

    arr = fall(arr)

def fall(A):
    temp = [0]*len(A)
    end_of_arr = 0
    
    for elem in A:
        if elem != 0:
            temp[end_of_arr] = elem
            end_of_arr += 1

    return temp

def print_arr():
    cnt = 0
    for elem in arr:
        if elem == 0:
            break
        else:
            cnt += 1
    
    print(cnt)
    for i in range(cnt):
        print(arr[i])


############

N = int(input())

for _ in range(N):
    arr.append(int(input()))

s1,e1 = map(int,input().split())
process(s1-1,e1-1)

#print(arr)

s2,e2 = map(int,input().split())
process(s2-1,e2-1)

#print(arr)

print_arr()