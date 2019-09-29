import sys
sys.stdin = open('2164.txt', 'r')

from collections import deque

N = int(input())

nums = deque()
for i in range(1, N + 1):
    nums.append(i)

leng = N

while leng != 1:
    nums.popleft()
    leng -= 1
    num = nums.popleft()
    nums.append(num)

print(nums[0])