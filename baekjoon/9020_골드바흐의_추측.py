import sys
sys.stdin = open('9020.txt')

import math

total_N = 10000
sieve = [True] * (total_N + 1)
sqrt_N = int(math.sqrt(total_N))

for num in range(2, sqrt_N + 1):
    if sieve[num]:
        for baesu in range(num + num, total_N + 1, num):
            sieve[baesu] = False

TC = int(input())
for tc in range(TC):
    N = int(input())
    opt_result = [-1, -1]
    min_diff = 1000000

    for one_num in range(2, N):
        if sieve[one_num]:
            other_num = N - one_num
            if other_num == 1:
                continue
            diff = abs(one_num - other_num)
            if sieve[other_num] and diff < min_diff:
                opt_result = [one_num, other_num]
                min_diff = diff
    
    opt_result.sort()
    print(f"{opt_result[0]} {opt_result[1]}")
print(sieve[:20])