mat = []

def is_possible_c_bo(pos):
    global mat
    x = pos[0]
    y= pos[1]
    if mat[x][y-1] == 1 or mat[x+1][y-1] == 1:
        return True

    # 왼쪽이 보이면
    left_ok = False
    right_ok = False
    if mat[x - 1][y] == 2:
        left_ok = True
    
    # 오른쪽이 보이면
    if mat[x + 1][y] == 2:
        right_ok = True
    # right ok
    # left ok & right ok 이면 ok
    return left_ok and right_ok
    

def is_possible_c_ki(pos):
    global mat
    x = pos[0]
    y = pos[1]
    return y == 0 or mat[x][y - 1] == 1 or mat[x - 1][y] == 2 or mat[x][y] == 2


def is_possible_d_ki(pos):
    global mat
    x = pos[0]
    y = pos[1]
    mat[x][y] -= 1
    # 위 기둥
    if mat[x][y + 1] == 1 or mat[x][y + 1] == 3:
        mat[x][y + 1] -= 1
        if not is_possible_c_ki([x, y + 1, 0]):
            mat[x][y + 1] += 1
            mat[x][y] += 1
            return False
        mat[x][y + 1] += 1
    # 오른쪽 보
    if mat[x][y + 1] == 2 or mat[x][y + 1] == 3:
        mat[x][y + 1] -= 2
        if not is_possible_c_bo([x, y + 1, 1]):
            mat[x][y + 1] += 2
            mat[x][y] += 1
            return False
        mat[x][y + 1] += 2
    # 왼쪽 보
    if mat[x - 1][y + 1] == 2 or mat[x - 1][y + 1] == 3:
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
        if mat[ki_x][ki_y] == 1 or mat[ki_x][ki_y] == 3:
            mat[ki_x][ki_y] -= 1
            if not is_possible_c_ki([ki_x, ki_y, 0]):
                mat[ki_x][ki_y] += 1
                mat[x][y] += 2
                return False
                
                            

        
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
                pass
            else: # 기둥
                if is_possible_d_ki(pos):
                    answer.remove(pos)

    
    print_mat(n)

    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))