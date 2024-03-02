import sys

ans_min = sys.maxsize
ans_max = -sys.maxsize

N = int(input())
operands = list(map(int,input().split()))
plus_num, minus_num, mul_num = map(int,input().split())
selected_operators = []

################################

def choose(n,plus,minus,mul):
    if n == N-1:
        calculate()
        return

    if plus != plus_num:
        selected_operators.append(0)
        choose(n+1,plus+1,minus,mul)
        selected_operators.pop()

    if minus != minus_num:
        selected_operators.append(1)
        choose(n + 1, plus, minus + 1, mul)
        selected_operators.pop()

    if mul != mul_num:
        selected_operators.append(2)
        choose(n + 1, plus, minus, mul+1)
        selected_operators.pop()

    return

def calculate():
    sum = operands[0]
    for i in range(1,N):
        if selected_operators[i-1] == 0:
            sum += operands[i]
        elif selected_operators[i-1] == 1:
            sum -= operands[i]
        else:
            sum *= operands[i]

    #print(selected_operators)
    #print(sum)

    global ans_min, ans_max
    ans_min = min(ans_min,sum)
    ans_max = max(ans_max,sum)
    return

################################
#print(operands)

choose(0,0,0,0)

print(ans_min,ans_max)