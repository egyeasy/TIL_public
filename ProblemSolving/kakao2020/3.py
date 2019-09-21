key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]

# 함수 참조 https://shoark7.github.io/programming/algorithm/rotate-2d-array
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def judge(lock_i, lock_j, len_lock, len_key, key, lock):
    # for i in range(len_key - lock_i - 1, len_key):
    #     for j in range(len_key - lock_j - 1, len_key):
    for i in range(len_lock):
        key_i = i - lock_i + 1
        if 0 <= key_i < len_key:
            for j in range(len_lock):
                key_j = j - lock_j + 1
                if 0 <= key_j < len_key:
                    if key[key_i][key_j] == lock[i][j]:
                        return False
                    elif lock[i][j] == 1 and key[key_i][key_j] == 0:
                        pass
                    elif lock[i][j] == 0 and key[key_i][key_j] == 1:
                        lock[i][j] = 2
                    else:
                        print("뭔가 잘못되었습니다")
    judge_result = True
    for i in range(len_lock):
        for j in range(len_lock):
            if lock[i][j] == 0:
                judge_result = False
            elif lock[i][j] == 2:
                lock[i][j] = 0
    return judge_result
            


def solution(key, lock):
    answer = False
    len_lock = len(lock)
    len_key = len(key)
    # print("key")
    # for i in key:
    #     print(i)
    # print()

    # print("lock")
    # for i in lock:
    #     print(i)
    # print()

    for i in range(len_lock + len_key - 1):
        for j in range(len_lock + len_key - 1):
            answer = judge(i, j, len_lock, len_key, key, lock)
            if answer == True:
                print("no rotate", i, j, answer)
                return answer

    for _ in range(1, 4):
        key = rotate_90(key)
        for i in range(len_lock + len_key - 1):
            for j in range(len_lock + len_key - 1):
                answer = judge(i, j, len_lock, len_key, key, lock)
                if answer == True:
                    print("rotate:", _, i, j, answer)
                    return answer
    print(answer)
    return answer

solution(key, lock)