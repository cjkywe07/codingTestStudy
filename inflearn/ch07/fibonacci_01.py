# fibonacci sequence(피보나치 수열)

'''반복문'''
def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    last = 1
    curr = 1

    for _ in range(3, n + 1):
        (last, curr) = (curr, last + curr)

    return curr


'''완전탐색(재귀)'''
# 불필요한 재계산 존재 - O(2^n)
def fibo_r(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo_r(n - 1) + fibo_r(n - 2)


'''DP'''
# 재계산 제거 - O(n)
# (1) Top-down 방식 (재귀 사용)
memo_1 = {}

def fibo_1(n):
    if n == 1 or n == 2:
        return 1
    
    if n not in memo_1:
        memo_1[n] = fibo_1(n - 1) + fibo_1(n - 2)

    return memo_1[n]


# (2) Bottom-up 방식 (반복문 사용)
memo_2 = {1: 1, 2: 1}

def fibo_2(n):
    for i in range(3, n + 1):
        memo_2[i] = memo_2[i - 1] + memo_2[i - 2]

    return memo_2[n]


print(fibo(7))
print(fibo_r(7))
print(fibo_1(7))
print(fibo_2(7))
