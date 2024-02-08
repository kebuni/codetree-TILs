N, K = map(int,input().split())

arr = [i for i in range(N+1)]
set_list = [set([i]) for i in range(N+1)]
switch_list = []

def print_set_list():
    for s in set_list:
        print(s)

for i in range(K):
    a, b = map(int,input().split())
    switch_list.append((a,b))

for a, b in switch_list:

    #print("현재 a에 앉아있는 애: ", arr[a])
    #print("현재 b에 앉아있는 애: ", arr[b])

    #set에 추가
    set_list[arr[a]].add(b)
    set_list[arr[b]].add(a)

    # arr상 위치 변경
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

#print_set_list()
for a, b in switch_list:

    #print("현재 a에 앉아있는 애: ", arr[a])
    #print("현재 b에 앉아있는 애: ", arr[b])

    #set에 추가
    set_list[arr[a]].add(b)
    set_list[arr[b]].add(a)

    # arr상 위치 변경
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

for a, b in switch_list:

    #print("현재 a에 앉아있는 애: ", arr[a])
    #print("현재 b에 앉아있는 애: ", arr[b])

    #set에 추가
    set_list[arr[a]].add(b)
    set_list[arr[b]].add(a)

    # arr상 위치 변경
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

for i in range(1,N+1):
    print(len(set_list[i]))