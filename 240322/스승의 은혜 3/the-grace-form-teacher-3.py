N, B = map(int, input().split())
gift_list = [tuple(map(int, input().split())) for i in range(N)]
ans = 0

for i in range(N):
    temp_list = gift_list[:]
    p, s = temp_list[i]
    temp_list[i] = (p // 2, s)

    temp_list.sort(key=lambda x: x[0] + x[1])
    #print(temp_list)

    price_sum = 0
    temp_ans = 0
    for j in range(N):
        price_sum += (temp_list[j][0] + temp_list[j][1])
        if price_sum > B:
            break
        else:
            temp_ans += 1

    ans = max(ans, temp_ans)

print(ans)