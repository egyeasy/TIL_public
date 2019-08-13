import sys
sys.stdin = open('2751.txt', 'r')

N = int(input())
nums = []
for i in range(N):
    num = int(input())
    nums.append(num)

nums.sort()

for num in nums:
    print(num)