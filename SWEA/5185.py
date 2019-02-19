"""
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110

> input
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

16진수 A부터 F는 대문자로 표시된다.

3
4 47FE
5 79E12
8 41DA16CD

> output
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101

"""

import sys
sys.stdin = open("5185.txt", "r")

T = int(input())

abcde = ["1", "2", "3", '4', '5', '6',
         '7', '8', '9', "A", "B", "C",
         "D", "E", "F"]

def find_num(alpha):
    length = len(abcde)
    i = 0
    for j in range(1, length+1):
        if abcde[i] == alpha:
            break
        i += 1
    return i + 1

for tc in range(1, T+1):
    num, hex = input().split()
    num = int(num)
    result = [0]*num*4
    # print(result)
    for digit in range(num):
        int_digit = find_num(hex[digit])
        # print(int_digit)
        for j in range(4):
            value = int_digit % 2
            # print(value, type(value))
            result[digit*4 + (3 - j)] = str(value)
            # print(result)
            int_digit //= 2

    print(f"#{tc} ", end="")
    len_result = len(result)
    for i in range(len_result):
        print(result[i], end="")

    print()


# idea
# 1.It's hard to designate variable name because there are int and string types, and hex and binary digits.
# So it's important to classify them clearly.



