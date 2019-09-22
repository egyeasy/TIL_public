import sys
sys.stdin = open('5.txt', 'r')

import math
# math.factorial(n)

N_row, N_col = map(int, input().split())
t_row, t_col = map(int, input().split())

if t_row > N_row or t_col > N_col:
    print("fail")
else:
    min_time = t_row + t_col
    print(min_time)
    cases = round(math.factorial(min_time) / (math.factorial(t_row) * math.factorial(t_col)))
    print(cases)