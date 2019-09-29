import sys
sys.stdin = open('2748.txt', 'r')


N = int(sys.stdin.readline())

first = 0
second = 1
third = 1

for i in range(N - 1):
    third = first + second
    first = second
    second = third

print(third)