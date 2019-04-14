global_min_cnt = 0

def backtrack(s, cnt, one_cnt):
    global global_min_cnt
    s_i = s // 10
    s_j = s % 10
    if s == 100:
        if one_cnt == total_ones and cnt < global_min_cnt:
            global_min_cnt = cnt
        return
    if cnt > global_min_cnt:
        return
    if mat[s_i][s_j] and not visited[s_i][s_j]:
        for size in range(5, 0, -1):
            # 정사각형을 찾았는지 여부
            judge = True
            for i in range(size):
                for j in range(size):
                    c_row = s_i + i
                    c_col = s_j + j
                    if c_row >= 10 or c_col >= 10 or not mat[c_row][c_col] or visited[c_row][c_col]:
                        judge = False
                        break
                if not judge:
                    break
            if judge:
                if storage[size - 1] > 0:
                    for i in range(size):
                        for j in range(size):
                            visited[s_i + i][s_j + j] = 1
                    storage[size - 1] -= 1
                    backtrack(s + 1, cnt + 1, one_cnt + (size ** 2))
                    for i in range(size):
                        for j in range(size):
                            visited[s_i + i][s_j + j] = 0
                    storage[size - 1] += 1
    else:
        backtrack(s + 1, cnt, one_cnt)

mat = [[0] * 10 for _ in range(10)]
total_ones = 0
for i in range(10):
    aline = list(map(int, input().split()))
    for j in range(10):
        if aline[j]:
            mat[i][j] = 1
            total_ones += 1

storage = [5, 5, 5, 5, 5]
visited = [[0] * 10 for _ in range(10)]
global_min_cnt = 1000000000

# 첫번째 인자 정수의 몫과 나머지를 행, 열로 사용
backtrack(0, 0, 0)

if global_min_cnt == 1000000000:
    print(-1)
else:
    print(global_min_cnt)