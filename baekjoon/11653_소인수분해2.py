# 1은 소인수분해 되지 않는다.

import sys
sys.stdin = open('11653.txt', 'r')

N = int(input())
divide = 2
# if N == 1:
#     print(1)
# else:
while N > 1:
    while N % divide != 0:
        divide += 1
    N //= divide
    print(divide)