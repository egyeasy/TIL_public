"""


> input


> output


"""
import sys
sys.stdin = open('14889.txt', 'r')


def CalPoint(nums, length):
    side_sum = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            side_sum += mat[nums[i]][nums[j]] + mat[nums[j]][nums[i]]
    return side_sum


side_N = int(input())
mat = [0] * side_N
for i in range(side_N):
    mat[i] = list(map(int, input().split()))

# for i in mat:
#     print(i)

total_min = 100000000
for i in range(1 << side_N):
    one_side = []
    other_side = []
    pass_judge = False
    for j in range(side_N):
        if i & (1 << j):
            if len(one_side) >= side_N:
                pass_judge = True
                break
            one_side.append(j)
        else:
            if len(other_side) >= side_N:
                pass_judge = True
                break
            other_side.append(j)
    if pass_judge:
        continue
    if len(one_side) == side_N // 2:
        # print(one_side, other_side)
        one_point = CalPoint(one_side, side_N // 2)
        other_point = CalPoint(other_side, side_N // 2)
        diff = abs(one_point - other_point)
        if diff < total_min:
            total_min = diff
            # print(one_side, other_side)

print(total_min)





# idea
# 1.