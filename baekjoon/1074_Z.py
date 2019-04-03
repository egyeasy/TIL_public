import sys
sys.stdin = open('1074.txt', 'r')


N, row_target, col_target = map(int, input().split())

curr_num = 2**N * 2**N - 1
curr_pos = [2**N - 1, 2**N - 1]
# print(curr_num, curr_pos)
for exp in range(N, -1, -1):
    changed = 0
    if curr_pos == [row_target, col_target]:
        break
    if row_target >= curr_pos[0] - (2 ** exp - 1) and col_target >= curr_pos[1] - (2 ** exp - 1):
        continue
    elif changed == 0:
        curr_pos[1] -= 2 ** exp
        curr_num -= (2 ** (exp * 2))
        changed += 1
    if row_target >= curr_pos[0] - (2 ** exp - 1) and col_target >= curr_pos[1] - (2 ** exp - 1):
        continue
    elif changed == 1:
        curr_pos[0] -= 2 ** exp
        curr_pos[1] += 2 ** exp
        curr_num -= (2 ** (exp * 2))
        changed += 1
    if row_target >= curr_pos[0] - (2 ** exp - 1) and col_target >= curr_pos[1] - (2 ** exp - 1):
        continue
    elif changed == 2:
        curr_pos[1] -= 2 ** exp
        curr_num -= (2 ** (exp * 2))
        changed += 1

print(curr_num)

# idea
# 1. traverse 2d array