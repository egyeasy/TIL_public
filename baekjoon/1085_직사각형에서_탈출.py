import sys
sys.stdin = open('1085.txt', 'r')

inputs = list(map(int, input().split()))

curr_pos = inputs[:2]
max_pos = inputs[2:4]

print(min([curr_pos[0], curr_pos[1], max_pos[0] - curr_pos[0], max_pos[1] - curr_pos[1]]))