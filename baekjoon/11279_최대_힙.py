# PriorityQueue는 느려서 통과 불가
# stdin.readline() 써야 통과

import sys
sys.stdin = open('11279.txt', 'r')

import heapq

que = []

N = int(input())
for i in range(N):
    comm = int(sys.stdin.readline())
    if comm == 0:
        if que:
            print(-heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, -comm)