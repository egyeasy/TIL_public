from collections import deque

dx = [1, 0]
dy = [0, 1]

dq = deque()
m = 4
n = 3
mat = []
total_cnt = 0
puddles = [[2, 2]]
visited = []

def dfs(s, m, n):
    global total_cnt, mat, visited
    visited[s[0]][s[1]] = 1

    print("visited")
    for i in visited:
        print(i)
    print()

    if s[0] == n - 1 and s[1] == m - 1:
        total_cnt += 1
        return

    for i in range(2):
        c_row = s[0] + dx[i]
        c_col = s[1] + dy[i]
        if 0 <= c_row < n and 0 <= c_col < m and not visited[c_row][c_col]:
            dfs([c_row, c_col], m, n)
            visited[c_row][c_col] = 0

            
        
def solution(m, n, puddles):
    global mat, total_cnt, visited
    mat = [[0] * m for _ in range(n)]
    
    mat[n - 1][m - 1] = 2
    
    for i in mat:
        print(i)

    visited = [[0] * m for _ in range(n)]
    for puddle in puddles:
        visited[puddle[1] - 1][puddle[0] - 1] = 1

    dfs([0, 0], m, n)
    print("total_cnt", total_cnt)
    
    answer = total_cnt % 1000000007
    
    return answer

print(solution(m, n, puddles))