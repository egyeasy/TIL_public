import sys
sys.stdin = open('2304.txt', 'r')

N = int(input())
lines = []
max_line = [0, 0]
for i in range(N):
    aline = list(map(int, input().split()))
    lines.append(aline)
    if aline[1] > max_line[1]:
        max_line = aline

lines = sorted(lines, key=lambda line:line[0])
max_idx = lines.index(max_line)

# for i in lines:
#     print(i)

total_area = 0
max_height = lines[0][1]

for i in range(max_idx + 1):
    if i < max_idx:
        if lines[i][1] > max_height:
            max_height = lines[i][1]
        area = (lines[i + 1][0] - lines[i][0]) * max_height
        total_area += area
    elif i == max_idx:
        total_area += lines[i][1]

max_height = lines[-1][1]
for i in range(N - 1, max_idx, -1):
    if lines[i][1] > max_height:
        max_height = lines[i][1]
    area = (lines[i][0] - lines[i - 1][0]) * max_height
    total_area += area

print(total_area)



