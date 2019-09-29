import sys
sys.stdin = open('6.txt', 'r')

position = -1

def print_n(number, garo):
    global position
    s_col = position
    sero = 2 * garo - 1
    if sorting == 'TOP':
        start_row = 0
    elif sorting == 'MIDDLE':
        start_row = (total_sero - sero) // 2
    else:
        start_row = total_sero - sero
    end_row = start_row + sero # 마지막 row + 1
    middle_row = (start_row + end_row) // 2
    end_col = s_col + garo

    # 도화지를 그린다
    # for row in range(start_row, end_row):
    #     for col in range(s_col , end_col):
    #         grid[row][col] = '.'

    # 숫자를 쓴다(함수)
    if number == 1:
        for row in range(start_row, end_row):
            grid[row][s_col + garo - 1] = '#'
    elif number == 2:
        for row in range(start_row, end_row):
            print(start_row, middle_row, end_row)
            if row == start_row or row == middle_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            elif row < middle_row:
                grid[row][s_col + garo - 1] = '#'
            elif row > middle_row:
                grid[row][s_col] = '#'
    elif number == 3:
        for row in range(start_row, end_row):
            if row == start_row or row == middle_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            else:
                grid[row][s_col + garo - 1] = '#'
    elif number == 4:
        for row in range(start_row, end_row):
            if row < middle_row:
                grid[row][s_col] = '#'
                grid[row][end_col - 1] = '#'
            elif row == middle_row:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            else:
                grid[row][end_col - 1] = '#'
    elif number == 5:
        for row in range(start_row, end_row):
            if row == start_row or row == middle_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            elif row < middle_row:
                grid[row][s_col] = '#'
            else:
                grid[row][s_col + garo - 1] = '#'
    elif number == 6:
        for row in range(start_row, end_row):
            if row == middle_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            elif row < middle_row:
                grid[row][s_col] = '#'
            else:
                grid[row][s_col] = '#'
                grid[row][s_col + garo - 1] = '#'
    elif number == 7:
        for row in range(start_row, end_row):
            if row == start_row:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            else:
                grid[row][s_col + garo - 1] = '#'
    elif number == 8:
        for row in range(start_row, end_row):
            if row == start_row or row == middle_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            else:
                grid[row][s_col] = '#'
                grid[row][s_col + garo - 1] = '#'
    elif number == 9:
        for row in range(start_row, end_row):
            if row == start_row or row == middle_row:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            elif row < middle_row:
                grid[row][s_col] = '#'
                grid[row][s_col + garo - 1] = '#'
            else:
                grid[row][s_col + garo - 1] = '#'
    elif number == 0:
        for row in range(start_row, end_row):
            if row == start_row or row == end_row - 1:
                for col in range(s_col, end_col):
                    grid[row][col] = '#'
            else:
                grid[row][s_col] = '#'
                grid[row][s_col + garo - 1] = '#'
    
    position += garo

    for row in range(total_sero):
        grid[row][position] = ' '

                
    
    # 마지막이 아니라면 공백 출력x(나중에 시도)

N_comm, sorting = input().split()
N_comm = int(N_comm)

comms = []
max_garo = 0
total_garo = 0

for i in range(N_comm):
    comm = input().split()
    comm[0] = int(comm[0])
    if comm[0] > max_garo:
        max_garo = comm[0]
    
    comm[1] = list(map(int, list(comm[1])))
    leng = len(comm[1])
    added = leng * comm[0] + leng - 1
    # print(added)
    total_garo += added

    comms.append(comm)

total_garo += N_comm
total_sero = 2 * max_garo - 1

grid = [['.'] * total_garo for _ in range(total_sero)]

# for i in grid:
#     print(i)

position = 0

for comm in comms:
    for num in comm[1]:
        print(comm[0], num)
        print_n(num, comm[0])
        position += 1
        print()


# for i in grid:
#     print(i)


for i in range(total_sero):
    for j in range(total_garo):
        print(grid[i][j], end='')
    print()