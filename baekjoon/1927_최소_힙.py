# input()은 시간 초과
import sys
import heapq
sys.stdin = open('1927.txt', 'r')

N = int(input())

heap = []

for i in range(N):
    comm = int(sys.stdin.readline().rstrip())
    if comm == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, comm)