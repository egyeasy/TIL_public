import sys
sys.stdin = open('2591.txt', 'r')

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    pop_item = stack[top]
    top -= 1
    return pop_item

def dfs(v):
    visited[v] = 1
    while v:
        w = 0
        for i in range(1, 3):
            if v + i < len_num:
                if i == 1:
                    w = v + i
                elif num[v] * 10 + num[v + 1] <= 34:
                    pass



num = list(map(int, list(input())))
print(num)
len_num = len(num)
stack = [0] * len_num
top = -1
visited = [0] * len_num




