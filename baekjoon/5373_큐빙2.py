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

the_cubic = {'U': up, 'D': down, 'F': front, 'B': back, 'L': left, 'R': right}


def rotate_the_face(the_face, is_plus):
    new_side = [[0] * 3 for _ in range(3)]
    if is_plus:
        for i in range(3):
            for j in range(3):
                new_side[j][2 - i] = the_cubic[the_face].data[i][j]
    else:
        for i in range(3):
            for j in range(3):
                new_side[2 - j][i] = the_cubic[the_face].data[i][j]
    for i in range(3):
        for j in range(3):
            the_cubic[the_face].data[i][j] = new_side[i][j]


def extract_side(side_face, side_dir, is_plus):
    
    if is_plus:

    else:
        pass


def rotate_sides(the_face, is_plus):
    side_list = ['upper', ]


def do_change(the_face, sign):
    if sign == '+':
        is_plus = True
    else:
        is_plus = False
    rotate_the_face(the_face, is_plus)
    rotate_sides(the_face, is_plus)


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
        do_change(command[0], command[1])

    print()