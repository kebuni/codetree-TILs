import sys

dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}
dic12 = {}
dic34 = {}
dic1234 = {}

N = int(input())
arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))
arr3 = list(map(int,sys.stdin.readline().split()))
arr4 = list(map(int,sys.stdin.readline().split()))

for elem in arr1:
    if elem in dic1:
        dic1[elem] += 1
    else:
        dic1[elem] = 1

for elem in arr2:
    if elem in dic2:
        dic2[elem] += 1
    else:
        dic2[elem] = 1

for elem in arr3:
    if elem in dic3:
        dic3[elem] += 1
    else:
        dic3[elem] = 1

for elem in arr4:
    if elem in dic4:
        dic4[elem] += 1
    else:
        dic4[elem] = 1

for key1 in dic1:
    for key2 in dic2:
        new_key = key1 + key2
        if new_key in dic12:
            dic12[new_key] += dic1[key1]*dic2[key2]
        else:
            dic12[new_key] = dic1[key1]*dic2[key2]

for key3 in dic3:
    for key4 in dic4:
        new_key = key3 + key4
        if new_key in dic34:
            dic34[new_key] += dic3[key3]*dic4[key4]
        else:
            dic34[new_key] = dic3[key3]*dic4[key4]

ans = 0
for key12 in dic12:
    if -key12 in dic34:
        ans += dic12[key12]*dic34[-key12]

print(ans)