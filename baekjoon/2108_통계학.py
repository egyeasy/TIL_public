import sys
sys.stdin = open('2108.txt', 'r')



N = int(input())
summ = 0
nums = []
dic = {}

for _ in range(N):
    num = int(sys.stdin.readline())
    if _ == 0:
        minn = num
        maxx = num
    else:
        if num > maxx:
            maxx = num
        elif num < minn:
            minn = num
    summ += num
    nums.append(num)
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

nums.sort()

first_most = 4001
second_most = 4001
for key, item in dic.items():
    if first_most == 4001:
        first_most = key
    elif item > dic[first_most]:
        first_most = key
        second_most = 4001
    elif item == dic[first_most]:
        if key <= first_most:
            second_most = first_most
            first_most = key
        elif key > first_most:
            if second_most == 4001:
                second_most = key
            elif key < second_most:
                second_most = key

print(round(summ / N))
print(nums[N // 2])
if second_most == 4001:
    print(first_most)
else:
    print(second_most)
print(maxx - minn)