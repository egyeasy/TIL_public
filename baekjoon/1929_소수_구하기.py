import sys
sys.stdin = open('1929.txt', 'r')

M, N = map(int, input().split())

# 홀수로 만들기

for num in range(M, N + 1):
    if num == 1:
        continue
    is_prime = True
    for div_num in range(2, num):
        if num % div_num == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
