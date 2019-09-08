import sys
sys.stdin = open('9461.txt', 'r')

T = int(input())
tcs = []
max_num = 0
for tc in range(T):
    num = int(sys.stdin.readline())
    tcs.append(num)
    if num > max_num:
        max_num = num

series = [0] * (max_num + 1)
series[1] = 1
series[2] = 1
series[3] = 1
series[4] = 2
series[5] = 2
series[6] = 3
series[7] = 4
series[8] = 5

for i in range(1, max_num + 1):
    if i <= 8:
        continue
    else:
        series[i] = series[i - 1] + series[i - 5]

for tc in tcs:
    print(series[tc])