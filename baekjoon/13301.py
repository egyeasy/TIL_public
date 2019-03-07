import sys
sys.stdin = open('13301.txt', 'r')

N = int(input())
memo = [0] * (N + 1)
memo[0], memo[1], memo[2] = 0, 1, 1

for i in range(3, N + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(2*(2 * memo[N] + memo[N - 1]))