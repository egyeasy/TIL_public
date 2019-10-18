import sys
sys.stdin = open('1874.txt', 'r')

from collections import deque

N = int(input())
comms = [0] * N
for i in range(N):
    comm = int(input())
    comms[i] = comm

stack = deque()
input_nums = list(range(1, N + 1))

result = []

for comm in comms:
    if input_nums and comm >= input_nums[0]:
        while input_nums and comm >= input_nums[0]:
            pop_item = input_nums.pop(0)
            stack.append(pop_item)
            result.append("+")
        stack.pop()
        result.append("-")
    else:
        if not stack or stack[-1] != comm:
            result = -1
            break
        else:
            stack.pop()
            result.append("-")
        

if result == -1:
    print("NO")
else:
    for i in result:
        print(i)
    
