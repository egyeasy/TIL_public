import sys
sys.stdin = open('10872.txt', 'r')

N = int(input())
factorial_N = 1

while N > 0:
    factorial_N *= N
    N -= 1

print(factorial_N)