dic = {}

N, M = map(int,input().split())

for i in range(1,N+1):
    string = input()
    dic[str(i)] = string
    dic[string] = str(i)

for i in range(M):
    command = input()
    print(dic[command])