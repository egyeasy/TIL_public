import sys
from collections import deque
sys.stdin = open('1966.txt', 'r')


def find_larger(num):
    for dq_item in dq:
        if dq_item[1] > num:
            return True
    return False

TC = int(input())
for tc in range(TC):
    N, target_M = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))

    dq = deque()

    for idx, num in enumerate(nums):
        dq.append((idx, num))
    
    # print(dq)
    pop_count = 0

    while True:
        item = dq[0]
        if find_larger(item[1]):
            dq.append(dq.popleft())
        elif item[0] == target_M:
            pop_count += 1
            break
        else:
            dq.popleft()
            pop_count += 1
        
        # print(dq)

    print(pop_count)

    # print()
        

    

    