# 불쾌한 날(Bad Hair Day)

import sys
sys.stdin = open("jeongol_1141.txt", "r")

stack = []
count = 0
N = int(input())
for i in range(N):
    num = int(input())
    if not stack:
        stack.append(num)
    else:
        while stack and stack[-1] <= num:
            stack.pop()
        count += len(stack)
        stack.append(num)

print(count)