#######
ans = 99999


#######

def cal_length(A):
    assert (len(A) > 0)

    cur = A[0]
    cnt = 1
    sum = 2

    for i in range(1, len(A)):
        if A[i] != cur:
            cur = A[i]
            cnt = 0
            sum += 2
        else:
            cnt += 1
            if cnt >= 10:
                sum += 1
    return sum


def Encoding(A, shift):

    B = A

    B_front = B[:-shift]
    B_end = B[-shift:]

    B = B_end + B_front
    #print(B)

    return cal_length(B)

#######

A = input()

for i in range(len(A)):
    ans = min(ans,Encoding(A,i))

print(ans)