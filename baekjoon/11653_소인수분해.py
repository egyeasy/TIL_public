# 1은 소인수분해 되지 않는다.

import sys
sys.stdin = open('11653.txt', 'r')

N = int(input())

if N != 1:
    while True:
        found = False
        half_N = N // 2
        for divide in range(2, half_N + 1):
            while N % divide == 0:
                print(divide)
                N //= divide
                found = True
        if not found:
            if N != 1:
                print(N)
            break
