"""
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

> 입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
20 30 10

> 출력
두 번째로 큰 정수를 출력한다.
20


"""

from sys import stdin

a = list(map(int, stdin.readline().rstrip().split(" ")))
a.sort()
print(a[1])


# 생각
# 1. stdin.readline()에 좀 더 익숙해지고자 계속 써봄