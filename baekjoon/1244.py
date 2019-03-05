import sys
sys.stdin = open('1244.txt', 'r')

def change(idx):
    if switches[idx]:
        switches[idx] = 0
    else:
        switches[idx] = 1

N = int(input())
switches = list(map(int, input().split()))
switches = [-1] + switches
# print(len(switches))
num = int(input())
for i in range(num):
    # print(switches)
    gender, idx = map(int, input().split())
    if gender == 1:
        each = idx
        while idx <= N:
            change(idx)
            # print(gender, idx, switches)
            idx += each
    else:
        dis = 0
        while idx - dis >= 1 and idx + dis <= N:
            if switches[idx - dis] == switches[idx + dis]:
                dis += 1
            else:
                break
        dis -= 1
        for i in range(idx - dis, idx + dis + 1):
            change(i)
        # print(gender, idx, dis, switches)
        # print(switches)


for i in range(1, N + 1, 20):
    print(' '.join(list(map(str, switches[i:i + 20]))))


