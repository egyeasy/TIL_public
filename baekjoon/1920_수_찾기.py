import sys
sys.stdin = open('1920.txt', 'r')

def bisec(num, start, end):
    global is_found
    # print(start, end)
    if start > end:
        # print("ended")
        return False
    mid = (start + end) // 2
    if N_nums[mid] == num:
        is_found = True
    elif num < N_nums[mid]:
        bisec(num, start, mid - 1)
    else:
        bisec(num, mid + 1, end)

N = int(input())
N_nums = list(map(int, input().split()))

M = int(input())
M_nums = list(map(int, input().split()))

N_nums.sort()

for m in M_nums:
    is_found = False
    bisec(m, 0, N - 1)
    if is_found:
        print(1)
    else:
        print(0)