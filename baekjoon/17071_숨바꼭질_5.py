import sys
sys.stdin = open('17071.txt', 'r')

from collections import deque

def bfs(subin, bro, time):
    dq.append([subin, bro, time])
    while dq:
        subin, bro, time = dq.popleft()
        if bro > 500000:
            return -1
        if subin == bro:
            return time
        cand1 = subin + 1
        cand2 = subin - 1
        cand3 = subin * 2
        if cand1 <= 500000:
            if not visited[cand1]:
                visited[cand1] = [bro]
                dq.append([cand1, bro + time + 1, time + 1])
            elif not bro in visited[cand1]:
                visited[cand1].append(bro)
                dq.append([cand1, bro + time + 1, time + 1])
        if cand2 >= 0:
            if not visited[cand2]:
                visited[cand2] = [bro]
                dq.append([cand2, bro + time + 1, time + 1])
            elif not bro in visited[cand2]:
                visited[cand2].append(bro)
                dq.append([cand2, bro + time + 1, time + 1])
        if cand3 <= 500000:
            # if cand3 < 0:
            #     print(subin, bro, time)
            #     return
            # print(subin, bro, time)
            # print(cand3)
            # print()
            if not visited[cand3]:
                visited[cand3] = [bro]
                dq.append([cand3, bro + time + 1, time + 1])
            elif not bro in visited[cand3]:
                visited[cand3].append(bro)
                dq.append([cand3, bro + time + 1, time + 1])
            

N, K = map(int, input().split())

visited = [0] * 500001
dq = deque()

answer = bfs(N, K, 0)
print(answer)