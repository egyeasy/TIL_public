# size 재는 법 최적화 가능
# case 예외 알아보기(같이 들어가고 나올때 등)

# import sys
# sys.stdin = open('3.txt', 'r')

from queue import PriorityQueue

que = PriorityQueue()

N = int(input())
nums = []
for i in range(N):
    num = tuple(map(int, input().split()))
    nums.append(num)

nums.sort(key=lambda x: (x[0], x[1]))

print(nums)
max_cnt = 0

for item in nums:
    if que.empty():
        que.put(item[1])
        size = que.qsize()
        if size > max_cnt:
            max_cnt = size
    else:
        peek = que.queue[0]
        if item[0] >= peek:
            que.get()
            que.put(item[1])
        else:
            que.put(item[1])
            size = que.qsize()
            if size > max_cnt:
                max_cnt = size

print(max_cnt)