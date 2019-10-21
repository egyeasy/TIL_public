import sys
from collections import deque
sys.stdin = open('5430.txt', 'r')

TC = int(input())
for tc in range(TC):
    comms = sys.stdin.readline().rstrip()
    N = int(input())
    if N == 0:
        nums = []
    else:
        nums = sys.stdin.readline().rstrip()[1:-1].split(',')
    # print(comms, nums)

    dq = deque()

    for num in nums:
        dq.append(num)

    # print(dq)

    is_rightside = True
    is_error = False

    for comm in comms:
        if comm == 'R':
            is_rightside = not is_rightside
        elif not dq:
            is_error = True
            break
        elif is_rightside:
            dq.popleft()
        else:
            dq.pop()
    
    if is_error:
        print('error')
    else:
        print('[', end='')
        if is_rightside:
            print(','.join(dq), end='')
        else:
            print(','.join(reversed(dq)), end='')
        print(']')
