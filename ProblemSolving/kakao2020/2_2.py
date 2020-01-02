# 200102

import sys
sys.stdin = open('2.txt', 'r')

from collections import deque

def is_right(word):
    dq = deque()
    for a in word:
        if a == '(':
            dq.append(a)
        else:
            if not dq:
                return False
            dq.pop()
    if dq:
        return False
    return True


def is_balanced(word):
    count_1 = 0
    count_2 = 0
    for a in word:
        if a == '(':
            count_1 += 1
        else:
            count_2 += 1
    if count_1 == count_2:
        return True
    else:
        return False

def judge(word):
    if not word:
        return ''
    else:
        leng = len(word)
        for i in range(1, leng + 1):
            cand = word[:i]
            if is_balanced(cand):
                u, v = cand, word[i:]
                if is_right(u):
                    result = judge(v)
                    print(u, result)
                    total_result = u + result
                    return total_result
                else:
                    total_result = '('
                    result = judge(v)
                    total_result += result + ')'
                    u = u[1:-1]
                    for i in u:
                        if i == '(':
                            total_result += ')'
                        else:
                            total_result += '('
                    return total_result


p = input()
answer = judge(p)

print(answer)
            