import sys
sys.stdin = open('2658.txt', 'r')

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def find(point):
    global judge
    row = point[0]
    col = point[1]
    direction = 100
    for dir in range(8):
        if mat[row + dx[dir]][col + dy[dir]]:
            direction = dir
            break
    if direction == 100:
        judge = False
    else:
        return direction

def go(point, dir):
    cand_row = point[0] + dx[dir]
    cand_col = point[1] + dy[dir]
    cand = mat[cand_row][cand_col]
    distance = 0
    while cand:
        # print(cand_row, cand_col)
        distance += 1
        cand_row += dx[dir]
        cand_col += dy[dir]
        cand = mat[cand_row][cand_col]
    new_point = [cand_row - dx[dir], cand_col - dy[dir]]

    return new_point, distance



mat = [[0] * 11 for _ in range(11)]
first = 0
area = 0

for i in range(10):
    aline = input()
    for j in range(10):
        if int(aline[j]):
            if not first:
                first = [i + 1, j + 1]
            mat[i + 1][j + 1] = int(aline[j])
            area += 1

# print(first)
# for _ in mat:
#     print(_)

judge = True

first_dir = find(first)
if not judge:
    print(0)
else:
    second, first_dis = go(first, first_dir)
    # print(first, second, first_dir, first_dis)

    second_dir = find(second)
    if not judge:
        print(0)
    else:
        third, second_dis = go(second, second_dir)
        # print(second, third, second_dir, second_dis)
    
        third_dir = find(third)
        if not judge:
            print(0)
        
        else:
            fourth, third_dis = go(third, third_dir)
            # print(third, fourth, third_dir, third_dis)
            
            if first != fourth:
                print(0)

            else:
                dis_list = sorted([first_dis, second_dis, third_dis])
                if dis_list[0] != dis_list[1]:
                    print(0)
                else:
                    if 2 * (dis_list[0] ** 2 + dis_list[1] ** 2) != third_dis ** 2:
                        print(0)
                    else:
                        if (dis_list[0] + 1) * (dis_list[1] + 1) != area:
                            print(0)
                        else:
                            print(first[0], first[1])
                            print(second[0], second[1])
                            print(third[0], third[1])







