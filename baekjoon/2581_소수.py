import sys
sys.stdin = open('2581.txt', 'r')

a = int(input())
b = int(input())

summ = 0
minn = -1

for num in range(a, b + 1):
    if num == 1:
        continue
    is_prime = True
    for div_num in range(2, num):
        if num % div_num == 0:
            is_prime = False
            break
    if is_prime:
        if minn == -1:
            minn = num
        summ += num

if minn == -1:
    print(-1)
else:
    print(summ)
    print(minn)

