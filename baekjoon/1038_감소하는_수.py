"""


> input


> output


"""

import sys
sys.stdin = open('1038.txt', 'r')

N = int(input())
if N > 1022:
    print(-1)
else:
    nums = []
    for i in range(1, 1 << 10):
        tmp = 0
        for j in range(9, -1, -1):
            if i & (1 << j):
                tmp = tmp * 10 + j
        nums.append(tmp)
        # nums[len(tmp)].append(sorted(tmp, reverse=True))
    nums.sort()
    # print(nums)
    print(nums[N])

# idea
# 1.