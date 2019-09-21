# LINE 2019 기출 해설 - 백준 특강 때 들었던 내용이랑 비슷한듯(홀짝 구분)
# 결국은 BFS를 기반으로 하되, 시간을 단축시킬 수 있는 방법을 찾아야 하는 것.
# 기본 알고리즘은 변하지 않는다.
import sys
sys.stdin = open('17071.txt', 'r')

from collections import deque

def bfs(subin, bro, time):
    global answer
    is_hol = 0
    dq.append([subin, bro, time])
    while dq:
        subin, bro, time = dq.popleft()
        # print(subin, bro, time)
        is_hol = time % 2
        if bro > 500000:
            return
        if visited[bro][is_hol]:
            # print(bro, visited[bro][is_hol])
            answer = time
            return
        cand_is_hol = (is_hol + 1) % 2
        cand1 = subin + 1
        cand2 = subin - 1
        cand3 = subin * 2
        if cand1 <= 500000:
            if not visited[cand1][cand_is_hol]:
                visited[cand1][cand_is_hol] = bro
                dq.append([cand1, bro + time + 1, time + 1])
        if cand2 >= 0:
            if not visited[cand2][cand_is_hol]:
                visited[cand2][cand_is_hol] = bro
                dq.append([cand2, bro + time + 1, time + 1])
        if cand3 <= 500000:
            if not visited[cand3][cand_is_hol]:
                visited[cand3][cand_is_hol] = bro
                dq.append([cand3, bro + time + 1, time + 1])
            

N, K = map(int, input().split())

visited = [[0] * 2 for _ in range(500001)]
# print(visited)
dq = deque()
answer = -1

visited[N][0] = 1

bfs(N, K, 0)
print(answer)