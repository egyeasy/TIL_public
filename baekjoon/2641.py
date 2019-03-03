import sys
sys.stdin = open('2641.txt', 'r')

def judge_line(base, alist):
    global judge
    for j in range(m):
        # print(alist[j:] + alist[:j])
        if base == alist[j:] + alist[:j]:
            judge = True

m = int(input())
base = list(map(int, input().split()))
n = int(input())
cnt = 0
result = []
for i in range(n):
    judge = False
    ori_aline = input()
    aline = list(map(int, ori_aline.split()))
    # print("base:", base)
    judge_line(base, aline)
    aline = [i + 2 if i < 3 else i - 2 for i in aline[::-1]]
    judge_line(base, aline)
    if judge:
        cnt += 1
        result.append(ori_aline)

print(cnt)
for i in result:
    print(i)