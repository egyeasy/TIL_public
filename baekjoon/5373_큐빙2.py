import sys
sys.stdin = open('5373.txt', 'r')


class face:
    def __init__(self, data, upper, downer, lefter, righter):
        self.data = data
        self.upper = upper
        self.downer = downer
        self.lefter = lefter
        self.righter = righter

#                                  data,  upper,   downer,   lefter,   righter
up = face([['w'] * 3 for _ in range(3)], [1, 'd'], [2, 'u'], [4, 'u'], [5, 'u'])
down = face([['y'] * 3 for _ in range(3)], [2, 'd'], [0, 'u'], [4, 'd'], [5, 'd'])
front = face([['r'] * 3 for _ in range(3)], [0, 'd'], [1, 'u'], [4, 'r'], [5, 'l'])
back = face([['o'] * 3 for _ in range(3)], [0, 'r'], [1, 'r'], [5, 'r'], [4, 'l'])
left = face([['g'] * 3 for _ in range(3)], [0, 'l'], [1, 'l'], [3, 'r'], [2, 'l'])
right = face([['b'] * 3 for _ in range(3)], [0, 'r'], [1, 'r'], [2, 'r'], [3, 'l'])


def judge_change(comm):
    which_side = -1
    is_plus = -1
    if comm[1] == '+':
        is_plus = True
    else:
        is_plus = False
    comm_side = comm[0]
    for side_idx in range(6):
        if comm_side == sides[side_idx]:
            which_side = side_idx
            return which_side, is_plus


def rotate_this_side(side_num, is_plus):
    new_side = [[0] * 3 for _ in range(3)]
    if is_plus:
        for i in range(3):
            for j in range(3):
                new_side[j][2 - i] = current_cubic[side_num][i][j]
    else:
        for i in range(3):
            for j in range(3):
                new_side[2 - j][i] = current_cubic[side_num][i][j]
    for i in range(3):
        for j in range(3):
            current_cubic[side_num][i][j] = new_side[i][j]


def do_change(side_num, is_plus):
    # 해당 면을 회전시킴
    rotate_this_side(side_num, is_plus)
    # 테두리 처리
    former_edge = [-1, -1, -1]
    this_edge = [-1, -1, -1]
    if is_plus:
        if side_num == 0:
            pass
        elif side_num == 2:
            pass
            
    else:
        pass

T = int(input())
for tc in range(T):
    # 정육면체 초기화 - 위, 아래, 앞, 뒤, 왼, 오
    current_cubic = [[[0] * 3 for __ in range(3)] for _ in range(6)]
    colors = ['w', 'y', 'r', 'o', 'g', 'b']
    sides = ['U', 'D', 'F', 'B', 'L', 'R']

    for idx in range(6):
        for i in range(3):
            for j in range(3):
                current_cubic[idx][i][j] = colors[idx]

    for _ in range(6):
        print(current_cubic[_])
    print()

    # input 처리
    num_changes = int(input())
    command_list = input().split()
    print(command_list)
    
    for command in command_list:
        side_num, is_plus = judge_change(command)
        do_change(side_num, is_plus)

    print()