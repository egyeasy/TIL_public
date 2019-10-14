import sys
# sys.stdin = open('11653.txt', 'r')

N = int(sys.stdin.readline().rstrip())

result = []

while True:
    found = False
    half_N = N // 2
    for divide in range(2, half_N + 1):
        if N % divide == 0:
            N //= divide
            result.append(divide)
            found = True
            break
    if not found:
        result.append(N)
        break

result.sort()

for num in result:
    print(num)