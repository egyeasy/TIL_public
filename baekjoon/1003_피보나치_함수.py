import sys

sys.stdin = open('1003.txt', 'r')

zero_cnt = -1
one_cnt = -1

result = [-1] * 41

def fibonacci(n):
    global zero_cnt, one_cnt
    if n == 0:
        # print("0")
        result[n] = (0, 1, 0) # 값, 0횟수, 1횟수
        zero_cnt += 1
        # return 0
    elif n == 1:
        # print("1")
        result[n] = (1, 0, 1)
        one_cnt += 1
        # return 1
    else:
        # if result != -1:
        #     zero_cnt += result[n][0]
        #     one_cnt += result[n][1]
        #     # return result[n][0]
        # else:
        result[n] = [result[n - 1][j] + result[n - 2][j] for j in range(3)]
        print("result n: ", result[n])
        # print(result)
        zero_cnt += result[n][1]
        one_cnt += result[n][2]
        # if n == 2:
        #     print(result)
        # return result[n - 1] + result[n - 2]


N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    zero_cnt = 0
    one_cnt = 0
    for i in range(n + 1):
        fibonacci(i)
    print(zero_cnt, one_cnt)