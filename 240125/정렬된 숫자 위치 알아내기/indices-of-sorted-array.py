import sys

n = int(input())

in_arr = list(map(int,sys.stdin.readline().split()))
arr = []
num_to_rank = [0]*(n+1)

for i in range(n):
    arr.append((in_arr[i],i+1))

arr.sort(key=lambda x:x[0])

for rank,(elem,num) in enumerate(arr,start=1):
    num_to_rank[num] = rank

# print(num_to_rank)
for i in range(1,n+1):
    print(num_to_rank[i],end=' ')