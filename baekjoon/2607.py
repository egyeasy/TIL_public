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
    for key, item in first_cnt.items():
        if key not in cand_cnt:
            cand_cnt[key] = -item
        else:
            cand_cnt[key] -= item
    # print(first_cnt)
    # print(cand_cnt)
    minus_one_finded = False
    plus_one_finded = False
    changed = False
    judge = True
    for item in cand_cnt.values():
        if item == 0:
            continue
        elif item == 1:
            if not changed:
                if plus_one_finded:
                    judge = False
                    break
                elif minus_one_finded:
                    minus_one_finded = False
                    changed = True
                else:
                    plus_one_finded = True
            else:
                judge = False
                break
        elif item == -1:
            if not changed:
                if minus_one_finded:
                    judge = False
                    break
                elif plus_one_finded:
                    plus_one_finded = False
                    changed = True
                else:
                    minus_one_finded = True
            else:
                judge = False
                break
        else:
            judge = False
            break
    
    if judge:
        # print("plus 1")
        total_cnt += 1

    # print()
        

print(total_cnt)