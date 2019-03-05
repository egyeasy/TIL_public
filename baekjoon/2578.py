import sys
sys.stdin = open('2578.txt', 'r')

def cnt_bingos():
    global cnt
    cnt = 0
    dig1_judge = True
    dig2_judge = True
    for i in range(5):
        row_judge = True
        col_judge = True
        for j in range(5):
            if mat[i][j]:
                row_judge = False
            if mat[j][i]:
                col_judge = False
            if i == j:
                if mat[i][j]:
                    dig1_judge = False
                if mat[i][4 - j]:
                    dig2_judge = False
        if row_judge:
            cnt += 1
        if col_judge:
            cnt += 1
    if dig1_judge:
        cnt += 1
    if dig2_judge:
        cnt += 1
    # print(cnt)
mat = [0] * 5

for i in range(5):
    aline = list(map(int, input().split()))
    mat[i] = aline

# for i in mat:
#     print(i)

calls = []
for i in range(5):
    aline = list(map(int, input().split()))
    calls += aline

# print(calls)
cnt = 0
total_judge = False
for call_idx in range(25):
    call = calls[call_idx]
    for i in range(5):
        for j in range(5):
            if mat[i][j] == call:
                mat[i][j] = 0
                cnt_bingos()
                if cnt >= 3:
                    total_judge = True
                    result = call_idx + 1
                    break
        if total_judge:
            break
    if total_judge:
        break

print(result)