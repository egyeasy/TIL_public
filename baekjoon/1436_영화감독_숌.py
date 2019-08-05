import sys
sys.stdin = open('1436.txt', 'r')

N = int(input())

count = 0
num = 1

sixes = '666'

while True:
    if sixes in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1