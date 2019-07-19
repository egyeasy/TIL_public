import sys
sys.stdin = open('2869.txt', 'r')

import math

day_up, night_down, tree_height = map(int, input().split())

diff = day_up - night_down
cnt_day = math.ceil((tree_height - day_up) / diff) + 1

print(cnt_day)