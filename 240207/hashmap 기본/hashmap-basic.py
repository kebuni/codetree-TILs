N = int(input())
dic = {}

for i in range(N):
    line = list(input().split())
    if line[0] == 'add':
        dic[int(line[1])] = int(line[2])
    elif line[0] == 'find':
        if int(line[1]) in dic:
            print(dic[int(line[1])])
        else:
            print("None")
    else:
        dic.pop(int(line[1]))