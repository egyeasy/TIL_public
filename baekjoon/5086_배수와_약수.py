import sys
sys.stdin = open('5086.txt', 'r')

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        isFactor = False
        isMultiple = False
        if b % a == 0:
            isFactor = True
        elif a % b == 0:
            isMultiple = True
        
        if isFactor:
            print("factor")
        elif isMultiple:
            print("multiple")
        else:
            print("neither")