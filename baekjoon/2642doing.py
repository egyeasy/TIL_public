import sys
sys.stdin = open('2642.txt', 'r')

mat = [0] * 6
for i in range(6):
    aline = list(map(int, input().split()))
    mat[i] = aline

for i in mat:
    print(i)

visited = [[0] * 6 for _ in range(6)]
judge = True
up_judge = True
for i in range(6):
    for j in range(6):
        if mat[i][j]:
            visited[i][j] = 1
            # 왼쪽 끝일 때
            
            # 위쪽 끝일 때
            if i + 2 < 6 and mat[i + 2][j]:
                visited[i + 2][j] = 1
                if mat[i + 1][j]:
                    visited[i + 1][j] = 1
                    if i + 3 < 6 and mat[i + 3][j]:
                        visited[i + 3][j] = 1
                        if visited:
                            pass
                    else:
                        pass

