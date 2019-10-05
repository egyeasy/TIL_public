import sys
sys.stdin = open('1966.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, target_M = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    # print()
    # print(nums)
    # print(N, target_M)

    t_priority = nums[target_M]


    reversed_nums = nums[::-1]
    reversed_target_M = N - target_M - 1
    first_larger_idx = -1

    for idx, num in enumerate(reversed_nums):
        if num > t_priority:
            first_larger_idx = N - idx - 1
            break    

    former_count = 0
    end_former_count = 0

    if target_M < first_larger_idx:
        for idx, num in enumerate(nums):
            if idx >= target_M:
                break
            if num == t_priority:
                former_count += 1
        
        for idx, num in enumerate(reversed_nums):
            if idx >= reversed_target_M or num > t_priority:
                break
            if num == t_priority:
                end_former_count += 1

    if first_larger_idx == -1:
        pass
    else:
        nums.sort(reverse=True)

        largest_count = 1

        for num in nums:
            if num <= t_priority:
                break
            largest_count += 1

        total_count = largest_count + former_count + end_former_count

    print(total_count)
    
            