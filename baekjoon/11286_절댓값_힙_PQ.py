import sys
sys.stdin = open('11286.txt', 'r')

from queue import PriorityQueue

N = int(input())
que = PriorityQueue()

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if que.empty():
            print(0)
        else:
            print(que.get()[1])
            
    else:
        que.put((abs(num), num))