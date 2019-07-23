import sys
sys.stdin = open('1978.txt', 'r')

N = int(input())

nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    # print("시작", num)
    if num == 1:
        continue
    for divide_num in range(2, num):
        # print(divide_num, end=" ")
        if num % divide_num == 0:
            # print("나눠짐")
            break
    else:
        cnt += 1
    # print()

print(cnt)