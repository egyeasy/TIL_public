"""


> input


> output


"""
import sys
sys.stdin = open('14863.txt', 'r')

N_cities, K_time = map(int, input().split())
values = [[[0] * 2 for __ in range(2)] for _ in range(N_cities)]
# print(values)
for i in range(N_cities):
    dobo_time, dobo_won, jajun_time, jajun_won = map(int, input().split())
    values[i][0] = [dobo_time, dobo_won]
    values[i][1] = [jajun_time, jajun_won]

# print(values)

# permutation
max_won = 0
for i in range(1 << N_cities):
    curr_time = 0
    curr_won = 0
    for j in range(N_cities):
        if i & (1 << j):
            # 1일 때 처리(자전거)
            curr_time += values[j][1][0]
            curr_won += values[j][1][1]
        else:
            # 0일 때 처리(도보)
            curr_time += values[j][0][0]
            curr_won += values[j][0][1]
        # 시간이나 돈 넘칠 때 가지치기
        if curr_time > K_time:
            break
    else:
        if curr_won > max_won:
            max_won = curr_won

print(max_won)

# idea
# 1.