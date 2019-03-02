import sys
sys.stdin = open('2659.txt', 'r')

def judge_num(num):
    str_num = str(num)
    judge = True
    for i in range(1, 4):
        transform = int(str_num[i:] + str_num[:i])
        if transform < num:
            judge = False

    return judge

nums = list(input().split())
minn = 10000
for i in range(4):
    num = int(''.join(nums[i:] + nums[:i]))
    if num < minn:
        minn = num

# print(minn)

# minn = [int(i) for i in str(minn)]
total = 0

for i in range(1111, minn + 1):
    if judge_num(i):
        total += 1

print(total)