import sys
sys.stdin = open('1021.txt', 'r')

start = -1
count = -1

def judge(target):
    global start, count
    tar_idx = target - 1
    left_count = 0
    right_count = 0
    minn = -1
    maxx = -1
    if tar_idx >= start:
        minn = start
        maxx = tar_idx
    else:
        minn = tar_idx
        maxx = start
    for i in range(minn, maxx):
        if nums[i]:
            left_count += 1
    for i in range(maxx, minn + N):
        i = i % N
        if nums[i]:
            right_count += 1
    count += left_count if left_count <= right_count else right_count
    nums[tar_idx] = 0
    start = (tar_idx + 1) % N


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
targets = list(map(int, input().split()))
start = 0
count = 0

for target in targets:
    judge(target)

print(count)