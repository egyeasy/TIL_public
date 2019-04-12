"""
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C,
60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

> 입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 자연수이다.
100

> 출력
시험 성적을 출력한다.
A

"""

point = int(input())
grades = ["A", "B", "C", "D", "F"]
for idx, grade in enumerate(grades):
    if point == 100:
        print("A")
        break
    if point < 60:
        print("F")
        break
    if 100-idx*10-10<= point <100-idx*10:
        print(grade)


# 생각
# 1. 코드 짧게 짜보려고 비효율적으로 짜보았다.
# 2. 생각 외의 고려할 지점들이 나타난다.