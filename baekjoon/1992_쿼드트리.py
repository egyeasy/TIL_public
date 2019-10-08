import sys
sys.stdin = open('1992.txt', 'r')

def search(s_row, s_col, size):
    starting_value = mat[s_row][s_col]
    for i in range(s_row, s_row + size):
        for j in range(s_col, s_col + size):
            if mat[i][j] != starting_value:
                return False
    if starting_value == 0:
        return 1
    else:
        return 2

def recursive(s_row, s_col, size):
    global result
    search_result = search(s_row, s_col, size)
    if not search_result:
        half_size = size // 2
        result += "("
        for i in range(2):
            for j in range(2):
                recursive(s_row + i * half_size, s_col + j * half_size, half_size)
        result += ")"
    elif search_result == 1:
        result += "0"
    else:
        result += "1"

N = int(input())
mat = [0] * N
for i in range(N):
    aline = list(map(int, sys.stdin.readline().rstrip()))
    mat[i] = aline

result = ""

recursive(0, 0, N)

print(result)