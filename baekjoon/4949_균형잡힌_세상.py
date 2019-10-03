import sys
sys.stdin = open('4949.txt', 'r')

from collections import deque

jjak = {']': '[', ')': '('}

while True:
    # 이상하게 이걸 쓰니까 출력 초과가 나타났다. rstrip을 해주면 통과함
    # words = sys.stdin.readline()
    words = sys.stdin.readline().rstrip()
    if words == '.':
        break

    dq = deque()
    result = 'yes'

    for a in words:
        if a == '[' or a == '(':
            dq.append(a)
        elif a == ']' or a == ')':
            if not dq:
                result = 'no'
            elif dq[-1] != jjak[a]:
                result = 'no'
            else:
                dq.pop()
    
    if dq:
        result = 'no'

    print(result)

            
            
