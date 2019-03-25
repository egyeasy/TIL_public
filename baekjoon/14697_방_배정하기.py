"""


> input


> output


"""
import sys
sys.stdin = open('14697.txt', 'r')

a, b, c, total = map(int, input().split())
a_N = total // a
b_N = total // b
c_N = total // c

for i in range(a_N + 1):
    tc_total = total
    tc_total -=



# idea
# 1.