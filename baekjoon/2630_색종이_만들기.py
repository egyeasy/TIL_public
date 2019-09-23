import sys
sys.stdin = open('2630.txt', 'r')

def part_judge(s_row, s_col, side, s_i, s_j):
    start_row = s_row + s_i * side
    start_col = s_col + s_j * side

    start = mat[start_row][start_col]
    all_same = True
    
    for i in range(side):
        for j in range(side):
            if mat[start_row + i][start_col + j] != start:
                all_same = False
                break
        if not all_same:
            break
    
    return all_same, start

def judge(s_row, s_col, side):
    global zero_cnt, one_cnt
    for i in range(2):
        for j in range(2):
            part_all_same, part_start = part_judge(s_row, s_col, side, i, j)
            if part_all_same:
                if part_start:
                    one_cnt += 1
                else:
                    zero_cnt += 1
            else:
                new_side = side // 2
                judge(s_row + side * i, s_col + side * j, new_side)


N = int(input())
mat = [[0] for _ in range(N)]

for i in range(N):
    aline = list(map(int, input().split()))
    mat[i] = aline

# for i in mat:
#     print(i)

zero_cnt = 0
one_cnt = 0

start = mat[0][0]
all_same = True

for i in range(N):
    for j in range(N):
        if mat[i][j] != start:
            all_same = False
            break
    if not all_same:
        break


if all_same:
    if start:
        one_cnt += 1
    else:
        zero_cnt += 1
else:
    judge(0, 0, N // 2)


print(zero_cnt)
print(one_cnt)