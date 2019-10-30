import sys
sys.stdin = open('[D5]3503.txt', 'r')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    idx = 2
    max_diff = -1

    # 홀수 번째에 있는 수를 오름차순으로 배열, 짝수번째를 최대값에서부터 내림차순으로 배열한다고 생각
    while idx < N:
        curr_diff = nums[idx] - nums[idx - 2]
        if curr_diff > max_diff:
            max_diff = curr_diff
        idx += 1
    
    # 최댓값, 그 바로 아랫값 비교
    curr_diff = nums[N - 1] - nums[N - 2]
    if curr_diff > max_diff:
        max_diff = curr_diff

    # 원형이므로 마지막 원소와 비교
    curr_diff = nums[1] - nums[0]
    if curr_diff > max_diff:
        max_diff = curr_diff

    print("#{} {}".format(tc, max_diff))