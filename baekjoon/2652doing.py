import sys
sys.stdin = open('2652.txt', 'r')

def find(i, j):
    i_ori = i
    j_ori = j
    # 가로로 0이 없을 때
    if mat[i][j + 1]:
        # visited 체크
        while mat[i][j]:
            while mat[i][j]:
                visited[i][j] = 1
                j += 1
            i += 1
            j = j_ori
        print(i, j)
        k, l = i_ori, j_ori
        # 빵꾸 뚫린 곳 찾기
        while mat[k][l]:
            # 가로로 이동
            while mat[k][l + 1]:
                l += 1
            # 세로로 이동하며 0 찾기
            while mat[k]:
                pass
                
    # 세로로 0이 없을 때
    else:
        pass

# go 특정 위치에서 주어진 길이만큼 이동하는 함수(도중에 벽 만나거나 1 만나면 return False)



m = int(input())
u, v, w, x, y = map(int, input().split())
mat = [0] * m

for i in range(m):
    aline = list(map(int, input().split()))
    mat[i] = aline

for i in mat:
    print(i)
    
visited = [[0] * m for _ in range(m)]

for i in range(m):
    for j in range(m):
        if mat[i][j]:
            find(i, j)