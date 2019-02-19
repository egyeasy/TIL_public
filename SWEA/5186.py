"""
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
13자리 이상이 필요한 경우에는‘overflow’를 출력하는 프로그램을 작성하시오.

> input
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다. 0

3
0.625
0.1
0.125

> output
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 101
#2 overflow
#3 001

"""

T = int(input())

for tc in range(1, T+1):
    num = input()
    float_num = float(num)
    index = -1
    for i in range(0, 13):
        if float_num * 2**i == int(float_num * 2**i):
            int_num = int(float_num * 2**i)
            index = i
            break
    # print(int_num, index)

    if index == -1:
        print(f"#{tc} overflow")
    else:
        result = [0] * index
        while index > 0:
            index -= 1
            result[index] = int_num % 2
            int_num //= 2
        print(f"#{tc} ", end="")
        for i in range(len(result)):
            print(result[i], end="")
        print()


# idea
# 1. The 'index' which represent number of shift also means the digit number below decimal point.


