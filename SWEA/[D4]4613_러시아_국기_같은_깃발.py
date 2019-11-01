import sys
sys.stdin = open('[D4]4613.txt', 'r')

from itertools import combinations

TC = int(input())
for tc in range(1, TC + 1):
    N_row, M_col = map(int, input().split())
    mat = [0] * N_row
    
    for i in range(N_row):
        aline = list(input())
        mat[i] = aline
        # print(aline)
    
    # 색이 바뀐 row의 set을 조합으로 구성
    combs = combinations(range(1, N_row), 2)
    min_count = 3000
    
    for comb in combs:
        # print(comb)
        start_row = 0
        curr_count = 0
        for idx, end_row in enumerate(comb):
            for i in range(start_row, end_row):
                for j in range(M_col):
                    if idx == 0:
                        if mat[i][j] != 'W':
                            curr_count += 1
                    else:
                        if mat[i][j] != 'B':
                            curr_count += 1
            start_row = end_row
        for i in range(start_row, N_row):
            for j in range(M_col):
                if mat[i][j] != 'R':
                    curr_count += 1
        if curr_count < min_count:
            min_count = curr_count
    
    print("#{} {}".format(tc, min_count))
    # print()