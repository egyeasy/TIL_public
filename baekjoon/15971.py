import sys
sys.stdin = open('15971.txt', 'r')

top = 0

def backS(s):
    global m, end, go_sum
    curr_sum = 0
    curr_max = 0
    visited[s] = 1
    print(f"s: {s}")
    value_assign = False
    while s:
        w = find_next(s)
        if w:
            push(s)
        while w:
            poped = False
            # if value_assign:
            #     curr_sum -= the_value
            the_value = matrix[s][w]
            curr_sum += the_value
            print(f"w: {w}")
            print(f"curr_sum: {curr_sum}")
            visited[w] = 1
            push(w)
            s = w
            w = find_next(s)
            if not w and s != end:
                curr_sum -= the_value
        s = pop()
        poped = True
        if poped:
            pass
        # if find_next(s) and s != end:
        #     curr_sum -= the_value
        print(f"pop ({s})")
    return curr_sum

def push(item):
    global top
    stack[top + 1] = item
    top += 1

def pop():
    global top
    top_item = stack[top]
    stack[top] = 0
    top -= 1
    return top_item

def find_next(s):
    global m
    for i in range(m + 1):
        if matrix[s][i] and not visited[i]:
            return i
    return 0

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
# for tc in range(1, 2):
for tc in range(1, T + 1):
    m, start, end = map(int, input().split())
    matrix = [[0] * (m + 1) for i in range(m + 1)]
    visited = [0] * (m + 1)
    stack =  [0] * m
    top = -1
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
    summ = backS(start)

    print(f"result: {summ}")
