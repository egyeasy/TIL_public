import sys
sys.stdin = open('1427.txt', 'r')

num = input()
num = sorted(num, reverse=True)
print(''.join(num))