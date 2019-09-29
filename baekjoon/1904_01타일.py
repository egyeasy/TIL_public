import sys
sys.stdin = open('1904.txt', 'r')

div = 15746

def fibonacci(n):
    for i in range(3, n + 1):
        results[i] = (results[i - 1] + results[i - 2]) % div
    return results[n]

N = int(input())

results = [0] * (N + 1)
results[1] = 1
results[2] = 2

result = fibonacci(N)

# print(results)
print(result % 15746)
