import sys
sys.stdin = open('2303.txt', 'r')

N = int(input())
max_of_all = 0
max_idx = -1
for stu_idx in range(N):
    nums = list(map(int, input().split()))
    # print(nums)
    stu_max = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                # stu_sum = sum([nums[i], nums[j], nums[k]]) % 10
                stu_sum = 0
                for m in [i, j, k]:
                    stu_sum += nums[m]
                stu_sum %= 10
                # print(i, j, k)
                # print(stu_sum, stu_max)
                if stu_sum > stu_max:
                    stu_max = stu_sum
    if stu_max >= max_of_all:
        max_of_all = stu_max
        max_idx = stu_idx
# print(max_of_all)
print(max_idx + 1)