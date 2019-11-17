# input() 시간 초과, PriorityQueue 시간 초과
import sys
import heapq
sys.stdin = open('11286.txt', 'r')


N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
            
    else:
        heapq.heappush(heap, (abs(num), num))