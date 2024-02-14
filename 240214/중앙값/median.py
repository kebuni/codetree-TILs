import heapq
import sys

T = int(input())

for x in range(T):

    N = int(input())
    arr = list(map(int,sys.stdin.readline().split()))
    right_min = []
    left_max = []
    median = arr[0]
    print(median,end=' ')

    for i in range(1,N):
        if arr[i] > median:
            heapq.heappush(right_min,arr[i])
        else:
            heapq.heappush(left_max,-arr[i])

        if i % 2 == 0:
            if len(right_min) > len(left_max): # median update
                heapq.heappush(left_max,-median)
                median = heapq.heappop(right_min)
            elif len(right_min) < len(left_max):
                heapq.heappush(right_min,median)
                median = -heapq.heappop(left_max)

            print(median,end=' ')

    print()