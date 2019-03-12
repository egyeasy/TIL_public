import sys
sys.stdin = open('15971.txt', 'r')


from collections import deque


def bfs(s):
    dq.append(s)
    visited[s[0]] = 1
    while dq:
        s = dq.popleft()
        st = s[0]
        for i in mat[st]:
            cand = i[0]
            if not visited[cand]:
                former[cand] = st
                # 최대거리 기록
                if i[1] >= visited[st]:
                    visited[cand] = i[1]
                else:
                    visited[cand] = visited[st]
                # 누적거리 기록
                for j in mat[former[st]]:
                    if j[0] == st:
                        i[1] += j[1]
                        break
                # 종결
                if cand == end:
                    for j in mat[st]:
                        if j[0] == cand:
                            print(j[1] - visited[cand])
                            return
                dq.append(i)
                    # for k in mat:
                    #     print(k)
                    # print()
                    # print(visited)


N, start, end = map(int, input().split())
mat = [[] for _ in range(N + 1)]
for i in range(N - 1):
    n_start, n_end, n_dis = map(int, input().split())
    mat[n_start].append([n_end, n_dis])
    mat[n_end].append([n_start, n_dis])

# for i in mat:
#     print(i)
# print()
dq = deque()
visited = [0] * (N + 1)
former = [0] * (N + 1)
if N <= 2:
    print(0)
else:
    bfs([start, 0])
# print(former)

# print()
# print(visited)
# print()
# for i in mat:
#     print(i)
# print()
