import sys
sys.stdin = open('2819.txt', 'r')

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(s_row, s_col, depth, word):
    dq.append((s_row, s_col, depth, word))
    while dq:
        s_row, s_col, depth, word = dq.popleft()
        if depth == 7:
            # print(word)
            result.append(word)
        else:
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if 0 <= c_row < 4 and 0 <= c_col < 4:
                    dq.append((c_row, c_col, depth + 1, word + str(mat[c_row][c_col])))
            
    

TC = int(input())
mat = [0] * 4

for tc in range(1, TC + 1):
    for i in range(4):
        aline = list(map(int, input().split()))
        mat[i] = aline
    
    result = []
    
    for i in range(4):
        for j in range(4):
            dq = deque()
            bfs(i, j, 0, '')
    
    print('#{} {}'.format(tc, len(set(result))))