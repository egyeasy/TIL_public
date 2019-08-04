import sys
sys.stdin = open('1018.txt', 'r')

M_row, N_col = map(int, input().split())

mat = [0] * M_row

for i in range(M_row):
    mat[i] = list(input())

min_count = 100000000

for stan_i in range(M_row - 7):
    for stan_j in range(N_col - 7):        
        count_W = 0
        count_B = 0

        for i in range(8):
            for j in range(8):
                if (stan_i + i) % 2 == 0:
                    if (stan_j + j) % 2 == 0:
                        if mat[stan_i + i][stan_j + j] == 'B':
                            count_W += 1
                        else:
                            count_B += 1
                    else:
                        if mat[stan_i + i][stan_j + j] == 'W':
                            count_W += 1
                        else:
                            count_B += 1
                else:
                    if (stan_j + j) % 2 == 0:
                        if mat[stan_i + i][stan_j + j] == 'W':
                            count_W += 1
                        else:
                            count_B += 1
                    else:
                        if mat[stan_i + i][stan_j + j] == 'B':
                            count_W += 1
                        else:
                            count_B += 1
        count = min(count_W, count_B)
        if count < min_count:
            min_count = count

# print(count_W, count_B)
print(min_count)
