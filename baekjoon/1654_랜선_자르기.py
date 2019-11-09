# 이분탐색
# 특정한 길이가 가능한지, 최적인지를 따지는 문제 -> 이분탐색으로 그 길이의 범위를 좁혀나가는 것

import sys
# sys.stdin = open('1654.txt', 'r')


def search(start, end):
    global answer
    if start > end:
        return
    mid = (start + end) // 2
    count = N
    for num in nums:
        count -= num // mid
    if count <= 0:
        if mid > answer:
            answer = mid
        search(mid + 1, end)
    else:
        search(start, mid - 1)
    
    

K, N = map(int, sys.stdin.readline().rstrip().split())
nums = []
max_num = 0

for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    if num > max_num:
        max_num = num


start = 1
end = max_num
answer = -1

search(start, end)

print(answer)