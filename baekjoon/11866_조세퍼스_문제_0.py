import sys
sys.stdin = open('11866.txt', 'r')

# from collections import deque

N, K = map(int, input().split())
dq = []

for i in range(1, N + 1):
    dq.append(i)

summ = sum(dq)

idx = -1
result = []

while summ:
    leng = K
    while leng:
        idx = (idx + 1) % N
        if dq[idx]:
            leng -= 1
    popped = dq[idx]
    dq[idx] = 0
    summ -= popped

    result.append(popped)
    
result = list(map(str, result))
print(f"<{', '.join(result)}>")