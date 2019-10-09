# 문제를 잘못 이해하고 등차수열로 푼 답안
import sys
sys.stdin = open('15650.txt', 'r')

N, M = map(int, input().split())

if M == 1:
    for num in range(1, N + 1):
        print(num)
else:
    for start_num in range(1, N + 1):
        for diff in range(1, N):
            curr_num = start_num
            series_count = 0
            nums = []
            while series_count < M and curr_num < N + 1:
                nums.append(str(curr_num))
                series_count += 1
                curr_num += diff
            if series_count == M:
                print(' '.join(nums))