import sys
sys.stdin = open('5373.txt', 'r')


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
            # 위 -> 오
            this_edge = [current_cubic[5][i][0] for i in range(3)]
            for i in range(3):
                current_cubic[5][i][0] = current_cubic[0][2][i]
            # 오 -> 아
            former_edge = this_edge[:]
            this_edge = [current_cubic[1][0][i] for i in range(3)]
            for i in range(3):
                current_cubic[1][0][i] = former_edge[i]
            # 아 -> 왼
            former_edge = this_edge[:]
            this_edge = [current_cubic[4][i][2] for i in range(3)]
            for i in range(3):
                current_cubic[4][i][2] = None
            
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