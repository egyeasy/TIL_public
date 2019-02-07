"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

> 입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
10 5
1 10 4 9 2 3 8 5 7 6

> 출력
1 4 2 3

"""

from sys import stdin

n, x = map(int, stdin.readline().rstrip().split(" "))
num_list = []
num_list = list(map(int, stdin.readline().rstrip().split(" ")))

for num in num_list:
    if x > num:
        print(num, end=" ")


# 생각
# 1. 특정 value x보다 큰 수를 list에서 찾는 메소드가 따로 없었다. 예상외로 직접 구현했어야.