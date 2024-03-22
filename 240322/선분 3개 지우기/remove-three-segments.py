N = int(input())
line_list = [tuple(map(int,input().split())) for i in range(N)]
original_arr = [0 for i in range(101)]

for a, b in line_list:
    for i in range(a,b+1):
        original_arr[i] += 1

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            
            temp_arr = original_arr[:]
            for x in [i,j,k]:
                a, b = line_list[x]
                for y in range(a,b+1):
                    temp_arr[y] -= 1

            if max(temp_arr) == 1:
                ans += 1

print(ans)