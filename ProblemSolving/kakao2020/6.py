# 2020.08.17
from collections import deque
answer = -1

def find(arr, dists, dis_i):
    global answer
    no_one = True
    for num in arr:
        if num == 1:
            no_one = False
            break
    if no_one and (answer == -1 or dis_i < answer):
        answer = dis_i
    else:
        if dis_i == len(dists):
            answer = -1
            return
        N = len(arr)
        for i, num in enumerate(arr):
            if num == 1 and i + dists[dis_i] + 1 < N:
                remember = deque()
                for j in range(i, i + dists[dis_i] + 1):
                    remember.append(arr[j])
                    arr[j] = 2
                find(arr, dists, dis_i + 1)
                for j in range(i, i + dists[dis_i] + 1):
                    arr[j] = remember.popleft()
    

def solution(n, weak, dist):
    global answer

    if len(weak) == 1:
        return answer

    wall = [0] * n

    for num in weak:
        wall[num] = 1

    max_distance = -1
    max_start = -1

    weak.append(n + weak[0])
    w_n = len(weak)
    for i in range(1, w_n):
        diff = weak[i] - weak[i - 1]
        print("i: ", i, "weak:", weak[i], "diff:", diff)
        if diff > max_distance:
            max_distance = diff
            max_start = i
    weak.pop()
    
    print("start:", max_start)
    print()
    
    arr = [0] * n
    idx = 0
    for i in range(max_start, max_start + n):
        real_idx = i % n
        arr[idx] = wall[real_idx]
        idx += 1

    print("arr:", arr)
    dist.sort(reverse=True)
    print("dist:", dist)
    find(arr, dist, 0)

    return answer

print("answer: ", solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))