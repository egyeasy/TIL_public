### failed - exceeded time limit ###

import sys
sys.stdin = open('2688.txt', 'r')

def backtrack(a, k, max_input):
    global max_len, RESULT, DONE
    if not DONE:
        if k == max_input:
            # print(a)
            result = judge_same(a)
            if result:
                RESULT = result
                max_len = len(result)
                DONE = True
        else:
            k += 1
            a[k] = 1
            backtrack(a, k, max_input)
            a[k] = 0
            backtrack(a, k, max_input)

def judge_same(a):
    one_list = [i + 1 for i in range(n) if a[i + 1]]
    two_list = [nums[i] for i in range(n) if a[i + 1]]
    # print(one_list, two_list)
    # print(f"one_list: {one_list}")
    # print(f"two_list: {sorted(two_list)}")
    if one_list == sorted(two_list):
        return one_list
        

n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
c = [0, 1]
# print(nums)
arr = [0] * (n + 1)
max_len = 0
RESULT = []
DONE = False
backtrack(arr, 0, n)
print(max_len)
for i in RESULT:
    print(i)