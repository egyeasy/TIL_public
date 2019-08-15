import sys
sys.stdin = open('10989.txt', 'r')

N = int(input())
counts = [0] * 10001
inputs = [-1] * N
outputs = [-1] * N

for i in range(N):
    num = int(input())
    inputs[i] = num
    counts[num] += 1

# update counts
for i in range(1, 10000):
    counts[i + 1] += counts[i]


for j in reversed(range(N)):
    outputs[counts[inputs[j]] - 1] = inputs[j]
    counts[inputs[j]] -= 1

print('\n'.join(map(str, outputs)))





# for i in range(N):
#     count = counts[i]
#     if count:
#         for _ in range(count):
#             print(i + 1)
