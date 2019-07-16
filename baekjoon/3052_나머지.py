import sys
sys.stdin = open('3052.txt', 'r')

nums = []
remains = []
for i in range(10):
    nums.append(int(input()))
    this_remain = nums[i] % 42
    if not this_remain in remains:
        remains.append(this_remain)

print(len(remains))