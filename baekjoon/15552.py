"""


> 입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
5
1 1
12 34
5 500
40 60
1000 1000

> 출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
2
46
505
100
2000

"""

from sys import stdin

num = int(stdin.readline().rstrip())

for i in range(num):
    value1, value2 = stdin.readline().split(" ")
    print(int(value1)+int(value2))


# 생각
# 1. input보다 효율적인 메소드를 활용하는 데에 적응하는 것이 까다로웠다.
# 2. 기본 작동 방식만 이해하면 나머지는 비슷한 듯.