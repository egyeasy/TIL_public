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
            # 왼쪽 끝일 때
            
            # 위쪽 끝일 때
            if i + 2 < 6:
                for k in range(i, i + 3):
                    if not mat[k][j]:
                        up_judge = False
                if up_judge:
                    for k in range(i + 1, 1):
                        pass