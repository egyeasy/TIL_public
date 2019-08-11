import sys
sys.stdin = open('2750.txt', 'r')

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)