"""


> input


> output


"""
import sys
sys.stdin = open('14889.txt', 'r')


def CalPoint(nums):
    side_sum = 0
    for i in range(half_leng - 1):
        for j in range(i + 1, half_leng):
            side_sum += mat[nums[i]][nums[j]] + mat[nums[j]][nums[i]]
    return side_sum


def comb(n, r):
    global total_min
    if r == 0:
        other_side = list(set(range(side_N)) - set(one_side))
        one_point = CalPoint(one_side)
        other_point = CalPoint(other_side)
        diff = abs(one_point - other_point)
        if diff < total_min:
            total_min = diff
    elif n < r:
        return
    else:
        one_side[r - 1] = n - 1
        comb(n - 1, r - 1)
        comb(n - 1, r)


side_N = int(input())
mat = [0] * side_N
for i in range(side_N):
    mat[i] = list(map(int, input().split()))

# for i in mat:
#     print(i)

total_min = 100000000
half_leng = side_N // 2
one_side = [0] * half_leng
comb(side_N, half_leng)

    # if len(one_side) == side_N // 2:
    #     one_point = CalPoint(one_side, side_N // 2)
    #     other_point = CalPoint(other_side, side_N // 2)
    #     diff = abs(one_point - other_point)
    #     if diff < total_min:
    #         total_min = diff

print(total_min)



# idea
# 1.