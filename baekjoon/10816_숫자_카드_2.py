import sys
sys.stdin = open('10816.txt', 'r')


def bisect(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if nums[mid] == target:
        counts[cnt_idx] += count_dict[target]
    elif nums[mid] > target:
        bisect(start, mid - 1)
    else:
        bisect(mid + 1, end)
    

N = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()

count_dict = {}

for num in nums:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

counts = [0] * M
cnt_idx = 0

for target in targets:
    start = 0
    end = N - 1
    bisect(start, end)
    cnt_idx += 1

for count in counts:
    print(count, end=" ")

print()