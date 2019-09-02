N = 5
stages = 	[2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    fails = [0] * (N + 2)
    for person in stages:
        # 지금까지 온 사람들을 모두 정리하고,
        for i in range(1, person + 1):
            # 전체 수에 더하고
            print(i)
            if fails[i]:
                fails[i][2] += 1
            else:
                fails[i] = [i, 0, 1]
            # 실패한 사람을 더함
        fails[person][1] += 1
    print(fails)
    for i in range(1, N + 1):
        if not fails[i]:
            fails[i] = [i, 0, 1]

    del fails[N + 1]
    del fails[0]

    print(fails)
    sort_fails = sorted(fails, key=lambda x: (x[1]/x[2], -x[0]), reverse=True)
    print(sort_fails)
    
    answer = []
    for item in sort_fails:
        answer.append(item[0])
    print(answer)
    return answer

solution(N, stages)