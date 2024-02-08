N = input()
set1 = set(map(int,input().split()))
M = input()
arr2 = list(map(int,input().split()))

for elem in arr2:
    if elem in set1:
        print(1)
    else:
        print(0)