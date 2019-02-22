import sys
sys.stdin = open('15971.txt', 'r')

def backS(s):
    global m, end, go_sum
    curr_sum = 0
    visited[s] = 1
    print(f"s: {s}")
    while s:
        w = find_next(s)
        if w:
            stk.push(s)
            dis_stk.push(matrix[s][w])
        while w:
            print(f"w: {w}")
            the_value = matrix[s][w]
            print(the_value)
            # curr_sum += the_value
            # print(f"curr_sum: {curr_sum}")
            visited[w] = 1
            stk.push(w)
            dis_stk.push(the_value)
            print(dis_stk.stack)
            s = w
            w = find_next(s)
            if w == end:
                dis_stk.push(matrix[s][w])
                return
            # if not w:
            #     curr_sum -= the_value
        s = stk.pop()
        dis_stk.pop()


class Stack:
    def __init__(self):
        self.stack = [0] * m
        self.top = -1

    def push(self, item):
        self.stack[self.top + 1] = item
        self.top += 1

    def pop(self):
        top_item = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
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
    stk = Stack()
    dis_stk = Stack()
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
    backS(start)

    print(f"result: {go_sum}")
    print(dis_stk.stack)