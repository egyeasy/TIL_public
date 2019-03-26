"""
정보 초등학교 6학년 여학생들은 단체로 2박 3일 수학여행을 가기로 했다.
학생들이 묵을 숙소에는 방의 정원(방 안에 있는 침대 수)을 기준으로 세 종류의 방이 있으며,
같은 종류의 방들이 여러 개 있다.
정보 초등학교에서는 학생들에게 이 방들을 배정하되, 배정된 모든 방에 빈 침대가 없도록 하고자 한다.

예를 들어, 방의 종류가 5인실, 9인실, 12인실이고 6학년 여학생 전체가 113명이라면,
5인실 4개, 9인실 5개, 12인실 4개를 예약하면 각 방에 남는 침대 없이 배정이 가능하다.
또한 12인실은 사용하지 않고 5인실 10개와 9인실 7개만 사용하는 것도 가능하다.
그러나 방의 종류가 3인실, 6인실, 9인실이고 6학년 여학생 전체가 112명이라면 빈 침대 없이 방을 배정하는 것은 불가능하다.

방의 정원을 나타내는 서로 다른 세 자연수와 전체 학생 수를 나타내는 자연수 하나가 주어졌을 때,
배정된 모든 방에 빈 침대가 없도록 방 배정이 가능한지를 결정하는 프로그램을 작성하시오.
단, 세 종류의 방은 모두 충분한 개수가 있다고 가정하며,
위의 예에서와 같이 세 종류의 방을 모두 활용하지 않고 한 종류 또는 두 종류의 방만 이용하여 배정하는 것도 허용한다.

> input
표준 입력으로 방의 정원을 나타내는 서로 다른 세 자연수 A, B, C (1 ≤ A < B < C ≤ 50)와
전체 학생 수를 나타내는 자연수 N (1 ≤ N ≤ 300)이 공백으로 분리되어 한 줄에 주어진다.

5 9 12 113

> output
빈 침대 없이 배정이 가능할 경우 표준 출력으로 1을, 불가능할 경우 0을 출력한다.

1

"""
import sys
sys.stdin = open('14697.txt', 'r')

a, b, c, total = map(int, input().split())
a_N = total // a
b_N = total // b
c_N = total // c

found = False

for i in range(a_N + 1):
    a_total = total
    a_total -= i * a
    # print("a", a_total, i * a)
    if a_total == 0:
        print(1)
        found = True
        break
    elif a_total < 0:
        break
    for j in range(b_N + 1):
        b_total = a_total
        b_total -= j * b
        # print("b", b_total, j * b)
        if b_total == 0:
            print(1)
            found = True
            break
        elif b_total < 0:
            break
        for k in range(c_N + 1):
            c_total = b_total
            c_total -= k * c
            # print("a", i * a, "b", j * b, "c", k * c, c_total)
            if c_total == 0:
                print(1)
                found = True
                break
            elif c_total < 0:
                break
        if found:
            break
    if found:
        break

if not found:
    print(0)

# idea
# 1. permutation for brute-force