import sys

sys.stdin = open('1003.txt', 'r')

zero_cnt = -1
one_cnt = -1
result = [-1] * 41
result[0] = (1, 0)
result[1] = (0, 1)

def fibonacci(n):
    global zero_cnt, one_cnt
    if n == 0 or n == 1:
        return
    else:
        for i in range(2, n + 1):
            this_zero_cnt = result[i - 1][0] + result[i - 2][0]
            this_one_cnt = result[i - 1][1] + result[i - 2][1]
            result[i] = (this_zero_cnt, this_one_cnt)

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    zero_cnt = 0
    one_cnt = 0
    fibonacci(n)
    print(result[n][0], result[n][1])