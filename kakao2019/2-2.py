def solution(N, stages):
    fails = {}
    for person in stages:
        # 지금까지 온 사람들을 모두 정리하고,
        for i in range(1, person + 1):
            # 전체 수에 더하고
            if i in fails:
                fails[i][1] += 1
            else:
                fails[i] = [0, 1]
            # 실패한 사람을 더함
        fails[person][0] += 1
    print(fails)
    for i in range(1, N + 1):
        if i not in fails:
            fails[i] = [0, 1]

    if N + 1 in fails:
        del fails[N + 1]

    print(list(fails.items()))
    sort_fails = sorted(fails.items(), key=lambda x: (x[1][0]/x[1][1], -x[0]), reverse=True)
    print(sort_fails)
    
    answer = []
    for item in sort_fails:
        answer.append(item[0])
    print(answer)
    return answer