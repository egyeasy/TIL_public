import sys
sys.stdin = open('2116.txt', 'r')

def find_across(idx):
    if idx == 0:
        return 5
    elif idx == 1:
        return 3
    elif idx == 2:
        return 4
    elif idx == 3:
        return 1
    elif idx == 4:
        return 2
    else:
        return 0

N = int(input())
dices = []
for i in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)

# for i in dices:
#     print(i)

results = []
for first_idx in range(6):
    each_result = 0
    down_idx = first_idx
    up_idx = find_across(first_idx)
    N_idx = 0
    while N_idx < N:
        aline = dices[N_idx]
        max_inline = 0
        for i in range(6):
            if i != down_idx and i != up_idx and aline[i] > max_inline:
                max_inline = aline[i]
        # print(N_idx, down_idx, up_idx, max_inline)
        each_result += max_inline
        N_idx += 1
        if N_idx < N:
            down_idx = dices[N_idx].index(aline[up_idx])
            up_idx = find_across(down_idx)
    results.append(each_result)
    # print()

# print(results)
print(max(results))