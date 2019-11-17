import sys
sys.stdin = open('10870.txt', 'r')


memo = [0] * 21
memo[1] = 1

def fibo(n):
    if n == 0:
        return memo[n]
    elif n == 1:
        return memo[n]
    else:
        if memo[n]:
            return memo[n]
        memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]

N = int(input())
print(fibo(N))
