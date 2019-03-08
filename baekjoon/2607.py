import sys
sys.stdin = open('2607.txt', 'r')

N = int(input())
first_word = input()
first_cnt = {}

for a in first_word:
    if a in first_cnt:
        first_cnt[a] += 1
    else:
        first_cnt[a] = 1
# print(first_cnt)
total_cnt = 0

for i in range(N - 1):
    cand = input()
    cand_cnt = {}
    for a in cand:
        if a in cand_cnt:
            cand_cnt[a] += 1
        else:
            cand_cnt[a] = 1
    # print(cand_cnt)
    check = True
    # one_life = True
    cnt = 0
    for key, item in cand_cnt.items():
        if key not in first_cnt:
            if one_life:
                cnt += 1
                if cnt >= 2:
                    check = False
                    break
            elif item == 1 and cnt == 1:
                continue
            else:
                check = False
                break
        elif first_cnt[key] == item:
            continue
        elif item - first_cnt[key] == 1:
            if one_life:
                cnt += 1
                if cnt >= 2:
                    check = False
                    break
            else:
                break

        elif item - first_cnt[key] == 1:
            if cnt == 1 and one_life:
                cnt = 0
                one_life = False
            else:
                check = False
                break

            if one_life:
                one_life = False
            else:
                check = False
                break
    if check:
        total_cnt += 1

print(total_cnt)
