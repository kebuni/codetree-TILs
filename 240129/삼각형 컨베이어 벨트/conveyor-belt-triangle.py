n, k = map(int, input().split())

k = k % (3*n)

arr = []

arr = arr+list(map(int,input().split()))
arr = arr+list(map(int,input().split()))
arr = arr+list(map(int,input().split()))

temp = arr[3*n-k : ]

for i in range(3*n-1,k-1,-1):
    #print("here",i)
    #print(arr[i],arr[i-k])
    arr[i] = arr[i-k]

#print(temp)
#print(arr)

for i in range(k):
    arr[i] = temp[i]

# print(arr)

for i in range(n):
    print(arr[i],end=' ')
print()
for i in range(n,2*n):
    print(arr[i],end=' ')
print()
for i in range(2*n,3*n):
    print(arr[i],end=' ')