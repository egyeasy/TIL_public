import sys
sys.stdin = open('15971.txt', 'r')

def backT(s, curr_sum, curr_max):
    global m, end, go_sum
    visited[s] = 1

    if s == end:
        print(s, end, curr_sum)
        go_sum = curr_sum
        return

    for i in range(m + 1):
        the_value = matrix[s][i]
        print(f"start:{s}, cand:{i}, value:{the_value}, curr_max:{curr_max}")
        if the_value and not visited[i]:
            if the_value > curr_max:
                the_max = curr_max
                print(f"curr_sum: {curr_sum + the_max}")
                backT(i, curr_sum + the_max, the_value)
            else:
                print(f"curr_sum: {curr_sum + the_value}")
                backT(i, curr_sum + the_value, curr_max)



T = int(input())
for tc in range(1, T + 1):
# for tc in range(1, 2):
    m, start, end = map(int, input().split())
    matrix = [[0] * (m + 1) for i in range(m + 1)]
    visited = [0] * (m + 1)
    for i in matrix:
        print(i)
    for i in range(m - 1):
        p_start, p_end, p_len = map(int, input().split())
        print(p_start, p_end, p_len)
        matrix[p_start][p_end] = p_len
        matrix[p_end][p_start] = p_len

    for i in matrix:
        print(i)
    go_sum = 0
    total_sum = 0
    backT(start, 0, 0)

    print(f"result: {go_sum}")
