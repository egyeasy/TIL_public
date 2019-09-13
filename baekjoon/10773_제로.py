import sys
sys.stdin = open('10773.txt', 'r')

stack = []

N = int(input())
for tc in range(N):
    comm = int(input())
    if comm == 0:
        stack.pop()
    else:
        stack.append(comm)

answer = sum(stack)
print(answer)
