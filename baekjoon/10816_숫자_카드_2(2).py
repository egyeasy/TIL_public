# 시간 초과(이상하게도 input()으로 받으면 틀렸다고 나옴 - 숫자를 제대로 못 읽는 듯)

import sys
sys.stdin = open('10816.txt', 'r')


def search_around(mid):
    counts[cnt_idx] += 1
    origin_mid = mid
    while mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
        counts[cnt_idx] += 1
        mid -= 1
    mid = origin_mid
    while mid + 1 < N and nums[mid + 1] == nums[mid]:
        counts[cnt_idx] += 1
        mid += 1

def bisect(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if nums[mid] == target:
        search_around(mid)
    elif nums[mid] > target:
        bisect(start, mid - 1)
    else:
        bisect(mid + 1, end)
    

N = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()
# print("sorted:", nums)

counts = [0] * M
cnt_idx = 0

for target in targets:
    start = 0
    end = N - 1
    bisect(start, end)
    cnt_idx += 1

counts = list(map(str, counts))

print(' '.join(counts))