import sys
sys.stdin = open('7568.txt', 'r')

N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = tuple(map(int, input().split()))

for i in range(N):
    count = 1
    for j in range(N):
        if i == j:
            continue
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            count += 1
    print(count, end=" ")
print()
