"""


> input


> output


"""
import sys
sys.stdin = open('11047.txt', 'r')

N_kinds, K_target = map(int, input().split())
kind_list = [0] * N_kinds
for i in range(N_kinds - 1, -1, -1):
    kind_list[i] = int(input())

# for i in kind_list:
#     print(i)

total_cnt = 0
for kind in kind_list:
    kind_gaesu = K_target // kind
    total_cnt += kind_gaesu
    K_target -= kind_gaesu * kind

print(total_cnt)


# idea
# 1.