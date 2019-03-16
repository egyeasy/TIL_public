"""


> input


> output


"""
import sys
sys.stdin = open('2491.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
max_length = 1
if N != 1:
    i = 0
    while i < N - 1: # index가 길이만큼 점프하도록 설정. 남은 길이가 최대 길이보다 작을 땐 중단.
        if N - i < max_length:
            break
        length = 1
        if nums[i] <= nums[i + 1]:
            length = 2
            curr_i = i + 1
            while curr_i + 1 < N and nums[curr_i] <= nums[curr_i + 1]:
                curr_i += 1
                length += 1
            if length > max_length:
                # print(i, "larger", length)
                max_length = length
        i += length
        # 아래꺼 while문 새로 분기하는 것 생각해보기.
    i = 0
    while i < N - 1:
        if N - i < max_length:
            break
        length = 1
        if nums[i] >= nums[i + 1]:
            # print(i, "smaller start")
            length = 2
            curr_i = i + 1
            while curr_i + 1 < N and nums[curr_i] >= nums[curr_i + 1]:
                curr_i += 1
                length += 1
            if length > max_length:
                # print(i, "small", length)
                max_length = length
        i += length
        

print(max_length)



# idea
# 1. 