import sys
sys.stdin = open('2477.txt', 'r')

fruit_num = int(input())
large = [0] * 5
small = [0] * 5
distances = []
dirs = []
overlaps = []
for i in range(6):
    dir, distance = map(int, input().split())
    distances.append([dir, distance])
    if dir in dirs:
        overlaps.append(dir)
    else:
        dirs.append(dir)

for i in range(6):
    if distances[i][0] not in overlaps:
        # print("starts", i, distances[i])
        distances = distances[i:] + distances[:i]
        break

for item in distances:
    dir, distance = item[0], item[1]
    if large[dir]:
        other_overlap = set(overlaps) - {dir}
        other_overlap = other_overlap.pop()
        if not small[other_overlap]:
            small[dir] = distance
        else:
            large[dir], small[dir] = distance, large[dir]
    else:
        large[dir] = distance

# print(large)
# print(small)

lg_side1 = 0
lg_side2 = 0
sm_side1 = 0
sm_side2 = 0
for i in range(1, 5):
    if not small[i]:
        if not lg_side1:
            lg_side1 = large[i]
        else:
            lg_side2 = large[i]
    else:
        if not sm_side1:
            sm_side1 = small[i]
        else:
            sm_side2 = small[i]

print(fruit_num * (lg_side1 * lg_side2 - sm_side1 * sm_side2))