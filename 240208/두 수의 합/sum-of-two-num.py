import sys

dic = {}

N, K = map(int,input().split())
line = list(map(int,sys.stdin.readline().split()))
deleted_dic = {}

for elem in line:
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1

ans = 0
for key in dic:
    #print("####",key,"####")
    if K-key == key:
        ans += dic[key] * (dic[key] - 1) // 2
        deleted_dic[key] = 0
        continue

    if K-key in dic and K-key not in deleted_dic and key not in deleted_dic:
        #print(K-key,' : ',dic[K-key])
        ans += dic[key]*dic[K-key]
        deleted_dic[key] = 0
        deleted_dic[K-key] = 0

print(ans)