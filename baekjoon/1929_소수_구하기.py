import sys
sys.stdin = open('1929.txt', 'r')

M, N = map(int, input().split())

# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
sieve = [True] * N
sqrt_N = int(N ** 0.5)

result = []

# n의 최대 약수가 sqrt(n) 이하이므로 sqrt(n)까지 검사
for num in range(2, sqrt_N  + 1):
    if sieve[num]:
        for j in range(num + num, N, num):
            pass
    
        
