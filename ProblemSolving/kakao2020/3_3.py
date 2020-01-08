mat = []

def init_mat(lock, len_key, len_lock):
    global mat
    for i in range(len_key - 1, len_key + len_lock):
        for j in range(len_key - 1, len_key + len_lock):
            #print(i, j)
            mat[i][j] = lock[i - len_key][j - len_key]

def set_key(s_i, s_j, key, len_key, len_lock):
    for mat_i in (s_i, s_i + len_key):
        for mat_j in (s_j, s_j + len_key):
            i = mat_i - s_i
            j = mat_j - s_j
            print("i, j : ", i, j)
            if key[i][j]:
                if mat[mat_i][mat_j]:
                    return False
                else:
                    mat[mat_i][mat_j] = 1
            else:
                if not mat[mat_i][mat_j]:
                    return False

def judge(len_key, len_lock):
    for i in range(len_key, len_key + len_lock - 1):
        for j in range(len_key, len_key + len_lock - 1):
            if not mat[i][j]:
                return False
    return True

def solution(key, lock):
    global mat
    len_key = len(key)
    len_lock = len(lock)
    len_mat = len_lock + 2 * (len_key - 1)
    answer = False
    for i in range(len_key + len_lock - 1):
        for j in range(len_key + len_lock - 1):
            mat = [[0] * len_mat for _ in range(len_mat)]
            print(mat)
            init_mat(lock, len_key, len_lock)
            print("init i, j: ", i, j)
            is_all_one = set_key(i, j, key, len_key, len_lock)
            if is_all_one:
                if judge(len_key, len_lock):
                    answer = True
                    break
        if answer:
            break
    
    while not answer:
        for _ in range(3):
            key = rotate_90(key)
            answer = False
            for i in range(len_key + len_lock - 1):
                for j in range(len_key + len_lock - 1):
                    mat = [[0] * len_mat for _ in range(len_mat)]
                    init_mat(lock, len_key, len_lock)
                    is_all_one = set_key(i, j, key, len_key, len_lock)
                    if is_all_one:
                        if judge(len_key, len_lock):
                            answer = True
                            break
                if answer:
                    break
                    
    return answer


key = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lock = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# key = [[1]]
# lock = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]

print(solution(key, lock))