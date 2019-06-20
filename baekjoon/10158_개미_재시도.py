import sys
sys.stdin = open('10158.txt', 'r')

# 북동, 북, 북서, 서, 남서, 남, 남동, 동
dir_x = [1, 0, -1, -1, -1, 0, 1, 1]
dir_y = [1, 1, 1, 0, -1, -1, -1, 0]

# 시작 방향은 북동
curr_dir = 0

def judge_wall():
    x, y = position
    # 북동쪽 코너(부터 반시계방향)
    if x == width and y == height:
        return 0
    elif 0 < x < width and y == height:
        return 1
    elif x == 0 and y == height:
        return 2
    elif x == 0 and 0 < y < height:
        return 3
    elif x == 0 and y == 0:
        return 4
    elif 0 < x < width and y == 0:
        return 5
    elif x == width and y == 0:
        return 6
    elif x == width and 0 < y < height:
        return 7
    # 벽이나 코너가 아닌 경우
    else:
        return -1

def change_dir(wall_num):
    global curr_dir
    if wall_num == 0:
        if curr_dir == 0:
            curr_dir = 4
    elif wall_num == 1:
        if curr_dir == 0:
            curr_dir = 6
        elif curr_dir == 1:
            curr_dir = 5
        elif curr_dir == 2:
            curr_dir = 4
    elif wall_num == 2:
        if curr_dir == 2:
            curr_dir = 6
    elif wall_num == 3:
        if curr_dir == 2:
            curr_dir = 0
        elif curr_dir == 3:
            curr_dir = 7
        elif curr_dir == 4:
            curr_dir = 6
    elif wall_num == 4:
        if curr_dir == 4:
            curr_dir = 0
    elif wall_num == 5:
        if curr_dir == 4:
            curr_dir = 2
        elif curr_dir == 5:
            curr_dir = 1
        elif curr_dir == 6:
            curr_dir = 0
    elif wall_num == 6:
        if curr_dir == 6:
            curr_dir = 2
    else:
        if curr_dir == 0:
            curr_dir = 2
        elif curr_dir == 6:
            curr_dir = 4
        elif curr_dir == 7:
            curr_dir = 3

def go():
    x, y = position
    # 1. 벽이나 코너가 아닌 경우
    wall_num = judge_wall()
    if wall_num == -1:
        pass
    # 2. 벽이나 코너인 경우
    else:
        # 방향을 바꿈
        change_dir(wall_num)
    # go
    position[0] += dir_x[curr_dir]
    position[1] += dir_y[curr_dir]

width, height = map(int, input().split())
position = list(map(int, input().split()))
origin = position[:]
time = int(input())
remain_time = time

while remain_time:
    go()
    if position == origin:
        remain_time = time % remain_time
    remain_time -= 1

print(position[0], position[1])