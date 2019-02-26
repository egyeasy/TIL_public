import sys
sys.stdin = open('2688.txt', 'r')

def dfs(s, arr):
    global start, RESULT
    visited[s] = 1
    # print(f"visited {s}, array: {arr}")
    for i in range(n + 1):
        if mat[s][i]:
            if i == start:
                # print("found")
                RESULT += arr
                # found = True
            elif not started[i] and not visited[i]:
                dfs(i, arr+[i])


n = int(input())
mat = [[0] * (n + 1) for i in range(n + 1)]
started = [0] * (n + 1)
for i in range(1, n + 1):
    mat[i][int(input())] = 1

# for i in mat:
#     print(i)

RESULT = []
for i in range(1, n + 1):
    if not started[i]:
        started[i] = 1
        visited = [0] * (n + 1)
        start = i
        result = [i]
        dfs(i, result)

# print(RESULT)
print(len(RESULT))
for i in sorted(RESULT):
    print(i)