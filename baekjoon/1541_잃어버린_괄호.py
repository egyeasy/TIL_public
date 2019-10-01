import sys
sys.stdin = open('1541.txt', 'r')

words = list(input())

minus_found = False
is_plus = True
result = 0
num = 0
for s in words:
    if s == '-':
        minus_found = True
        if is_plus:
            result += num
        else:
            result -= num
        num = 0
        is_plus = False
    elif s == '+':
        if minus_found:
            is_plus = False
        else:
            is_plus = True
        if is_plus:
            result += num
        else:
            result -= num
        num = 0
    else:
        num = num * 10 + int(s)

if is_plus:
    result += num
else:
    result -= num

print(result)