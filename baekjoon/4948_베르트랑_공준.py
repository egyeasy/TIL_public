import sys
sys.stdin = open('4948.txt', 'r')

import math

while True:
    N = int(input())
    if N == 0:
        break
    double_N = 2 * N
    sqrt_N = int(math.sqrt(double_N))

    sieve = [True] * (double_N + 1)

    for num in range(2, sqrt_N + 1):
        if sieve[num]:
            # print(num)
            for baesu in range(num + num, double_N + 1, num):
                sieve[baesu] = False
    
    # print(sieve)
    print(sum(sieve[N + 1:double_N + 1]))
    # print()
