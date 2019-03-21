"""


> input


> output


"""
import sys
sys.stdin = open('6988.txt', 'r')


def go(s):
    global total_max
    for i in range(s + 1, N_num - 1):
        diff = nums[i] - nums[s]
        go_times = 2
        part_sum = nums[s] + nums[i]
        go_i = i + 1
        former_num = nums[i]
        while go_i < N_num:
            if nums[go_i] == former_num + diff:
                part_sum += nums[go_i]
                former_num = nums[go_i]
                go_times += 1
            elif nums[go_i] > former_num + diff:
                break
            go_i += 1
        if go_i >= 3 and part_sum > total_max:
            total_max = part_sum


N_num = int(input())
nums = list(map(int, input().split()))

total_max = 0
for i in range(N_num - 2):
    # visited = [0] * N_num
    go(i)

print(total_max)



# idea
# 1.