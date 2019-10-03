import sys
sys.stdin = open('1037.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
minn = 1000001
maxx = 0

if N == 1:
    result = nums[0] ** 2
else:
    for num in nums:
        if num < minn:
            minn = num
        if num > maxx:
            maxx = num
    result = minn * maxx

print(result)