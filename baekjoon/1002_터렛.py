import sys
sys.stdin = open('1002.txt', 'r')

import math

T = int(input())
for tc in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    # print(x_1, y_1, r_1, x_2, y_2, r_2)
    # print((x_1 - x_2)**2 + (y_1 - y_2)**2)
    distance = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    if distance > r_1 + r_2 or distance + min(r_1, r_2) < max(r_1, r_2):
        print(0)
    elif distance == 0 and r_1 == r_2:
        print(-1)
    elif distance == r_1 + r_2 or distance + min(r_1, r_2) == max(r_1, r_2):
        print(1)
    else:
        print(2)
    
