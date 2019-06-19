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


def do_change(side_num, is_plus):
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