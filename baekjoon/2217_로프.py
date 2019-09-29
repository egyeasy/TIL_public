import sys
sys.stdin = open('2217.txt', 'r')

N = int(input())
weights = []
for i in range(N):
    weight = int(sys.stdin.readline())
    weights.append(weight)

weights.sort(reverse=True)
total_max = 0

for cnt, weight in enumerate(weights):
    curr_max = (cnt + 1) * weight
    if curr_max > total_max:
        total_max = curr_max
    # 아래 문을 넣으면 반례 존재
    # else:
    #     break

print(total_max)