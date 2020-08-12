# 2020.08.12 통과

mat = []

def is_ok(x, y):
    n = len(mat)
    return 0 <= x < n and 0 <= y < n

def is_ki(x, y):
    return mat[x][y] == 1 or mat[x][y] == 3

def is_bo(x, y):
    return mat[x][y] == 2 or mat[x][y] == 3

def is_possible_c_bo(pos):
    global mat
    x = pos[0]
    y= pos[1]
    if (is_ok(x, y-1) and is_ki(x, y-1)) or (is_ok(x+1, y-1) and is_ki(x+1, y-1)):
        return True

    # 왼쪽이 보이면
    left_ok = False
    right_ok = False
    if is_ok(x - 1, y) and is_bo(x-1, y):
        left_ok = True
    
    # 오른쪽이 보이면
    if is_ok(x+1, y) and is_bo(x+1, y):
        right_ok = True
    # right ok
    # left ok & right ok 이면 ok
    return left_ok and right_ok
    

def is_possible_c_ki(pos):
    global mat
    x = pos[0]
    y = pos[1]
    return y == 0 or (is_ok(x, y-1) and is_ki(x, y-1)) or\
        (is_ok(x-1, y) and is_bo(x-1, y)) or\
            (is_ok(x, y) and is_bo(x, y))


def is_possible_d_ki(pos):
    global mat
    x = pos[0]
    y = pos[1]
    mat[x][y] -= 1
    # 위 기둥
    if is_ok(x, y+1) and is_ki(x, y+1):
        mat[x][y + 1] -= 1
        if not is_possible_c_ki([x, y + 1, 0]):
            mat[x][y + 1] += 1
            mat[x][y] += 1
            return False
        mat[x][y + 1] += 1
    # 오른쪽 보
    if is_ok(x, y+1) and is_bo(x, y+1):
        mat[x][y + 1] -= 2
        if not is_possible_c_bo([x, y + 1, 1]):
            mat[x][y + 1] += 2
            mat[x][y] += 1
            return False
        mat[x][y + 1] += 2
    # 왼쪽 보
    if is_ok(x-1, y+1) and is_bo(x-1, y+1):
        mat[x - 1][y + 1] -= 2
        if not is_possible_c_bo([x - 1, y + 1, 1]):
            mat[x - 1][y + 1] += 2
            mat[x][y] += 1
            return False
        mat[x - 1][y + 1] += 2
    return True
        

def is_possible_d_bo(pos):
    global mat
    x = pos[0]
    y = pos[1]
    mat[x][y] -= 2
    # 후보 기둥 처리
    kis_x = [x, x, x + 1, x + 1]
    kis_y = [y, y + 1, y, y + 1]
    for i in range(4):
        ki_x = kis_x[i]
        ki_y = kis_y[i]
        if is_ok(ki_x, ki_y) and is_ki(ki_x, ki_y):
            mat[ki_x][ki_y] -= 1
            if not is_possible_c_ki([ki_x, ki_y, 0]):
                mat[ki_x][ki_y] += 1
                mat[x][y] += 2
                return False
            mat[ki_x][ki_y] += 1

    bos_x = [x - 1, x + 1]
    bos_y = [y, y]
    for i in range(2):
        bo_x = bos_x[i]
        bo_y = bos_y[i]
        if is_ok(bo_x, bo_y) and is_bo(bo_x, bo_y):
            mat[bo_x][bo_y] -= 2
            if not is_possible_c_bo([bo_x, bo_y, 1]):
                mat[bo_x][bo_y] += 2
                mat[x][y] += 2
                return False
            mat[bo_x][bo_y] += 2

    return True
        
def print_mat(n):
    global mat
    for i in range(n + 1):
        for j in range(n + 1):
            print(mat[j][n - i], end=" ")
        print()

def solution(n, build_frame):
    global mat
    answer = []
    mat = [[0] * (n + 1) for _ in range(n + 1)]
    for frame in build_frame:
        pos = frame[:3]
        x = pos[0]
        y = pos[1]
        if frame[3]: # 설치
            if frame[2]: # 보
                if is_possible_c_bo(pos):
                    mat[pos[0]][pos[1]] = 2 if not mat[pos[0]][pos[1]] else 3
                    answer.append(pos)
            else: # 기둥
                if is_possible_c_ki(pos):
                    mat[pos[0]][pos[1]] = 1 if not mat[pos[0]][pos[1]] else 3
                    answer.append(pos)
        else: # 삭제
            if frame[2]: # 보
                if is_possible_d_bo(pos):
                    answer.remove(pos)
            else: # 기둥
                if is_possible_d_ki(pos):
                    answer.remove(pos)
    
    print_mat(n)

    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))