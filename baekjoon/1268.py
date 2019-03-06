import sys
sys.stdin = open('1268.txt', 'r')

N = int(input())
mat = [[0] * N for _ in range(5)]

for i in range(N):
    aline = list(map(int, input().split()))
    for j in range(5):
        mat[j][i] = aline[j]

cnts = [[] for _ in range(N)]

for grade in range(5):
    check = []
    for stu in range(N):
        the_class = mat[grade][stu]
        for ch in check:
            if ch[0] == the_class:
                if ch[1] not in cnts[stu]:
                    cnts[stu].append(ch[1])
                    cnts[ch[1]].append(stu)
        check.append((the_class, stu))

max_cnt = 0
max_idx = 0
for i in range(N):
    length = len(cnts[i])
    if length > max_cnt:
        max_cnt = length
        max_idx = i

print(max_idx + 1)


