import sys
sys.stdin = open('2302.txt', 'r')

def fibo(n):
    if memo[n]:
        return memo[n]
    else:
        value = fibo(n - 1) + fibo(n - 2)
        memo[n] = value
        return value

N = int(input())
fixed_M = int(input())
memo = [1] + [0] * (N)
memo[1], memo[2] = 1, 2
result = 1
former = 0

for i in range(fixed_M):
    m = int(input())
    result *= fibo(m - former - 1)
    # print(former, m, m - former - 1, fibo(m - former - 1))
    former = m

result *= fibo(N - former)
print(result)
