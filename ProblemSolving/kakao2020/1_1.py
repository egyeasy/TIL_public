# 200101 풀어본 것. 답안 통과. 코너케이스 다 피해감

import sys
sys.stdin = open('1.txt', 'r')

curr_idx = -1

s = input()



length = len(s)
result = [0] * length
for leng in range(1, length):
    stan = s[:leng]
    curr_idx = leng
    gaesu = 1
    new_word = ""
    end_added = False
    while curr_idx < length:
        next = s[curr_idx: curr_idx + leng]
        if stan == next:
            gaesu += 1
            curr_idx += leng
        else:
            if gaesu == 1:
                new_word += stan
            else:
                new_word += str(gaesu) + stan
                gaesu = 1
            stan = s[curr_idx: curr_idx + leng]
            curr_idx += leng
    if gaesu == 1:
        new_word += stan
    else:
        new_word += str(gaesu) + stan
    result[leng] = len(new_word)
    print(leng, new_word)

print(result)
if length == 1:
    print(1)
else:
    print(min(result[1:]))
        