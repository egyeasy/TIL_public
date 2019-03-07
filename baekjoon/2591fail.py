import sys
sys.stdin = open('2591.txt', 'r')
import time
from collections import deque
s = time.time()
def bfs(s):
    global total_cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        # if not visited[s]:
        #     visited[s] = 1
        # print("visited", s)
        if s == len_num - 1:
            total_cnt += 1
            # print("total", total_cnt, "s", s, "i", i)
            continue
        for i in [1, 2]:
            if s + i <= len_num - 1:
                if i == 1:
                    # print("한글자", "s", s, "i", i)
                    dq.append(s + i)
                elif num[s + 1] * 10 + num[s + 2] <= 34:
                    # print("두글자", "s", s, "i", i, "값", num[s + 1] * 10 + num[s + 2])
                    dq.append(s + i)


num = list(map(int, list(input())))
# print(num)
len_num = len(num)
dq = deque()
visited = [0] * len(num)
total_cnt = 0
bfs(-1)
print(total_cnt)
print(time.time() - s)