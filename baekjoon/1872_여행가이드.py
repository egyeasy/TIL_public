import sys
sys.stdin = open('1872.txt', 'r')

from math import *


def perm(n, k):
    global time, guide_position, go_back_times, min_last_arrival_time
    if k == n:
        print(nums)
        guide_position = [0, 0]
        time = 0
        for num in nums:
            go_to(num)
        print(go_back_times)
        print()

        last_arrival_time = max(go_back_times)
        if last_arrival_time < min_last_arrival_time:
            min_last_arrival_time = last_arrival_time
            # min_go_back_times = go_back_times
    else:
        for i in range(k, n):
            nums[k], nums[i] = nums[i], nums[k]
            perm(n, k + 1)
            nums[k], nums[i] = nums[i], nums[k]


def go_to(traveler):
    global time, guide_position, last_arrival_time
    trav_x, trav_y, trav_velocity, trav_angle = information_travelers[traveler]
    trav_x += trav_velocity * cos(trav_angle) * time
    trav_y += trav_velocity * sin(trav_angle) * time
    guide_x, guide_y = guide_position
    print("traveler", traveler, ":", information_travelers[traveler], guide_position)

    # a*t^2 + 2b*t + c = 0의 해 구하기
    a = trav_velocity ** 2 - guide_velocity ** 2
    b = trav_velocity * ((trav_x - guide_x) * cos(trav_angle) + (trav_y - guide_y) * sin(trav_angle))
    c = (trav_x - guide_x) ** 2 + (trav_y - guide_y) ** 2

    # 근의 공식
    plus_time = (-b + sqrt(b ** 2 - a * c)) / a
    minus_time = (-b - sqrt(b ** 2 - a * c)) / a
    go_time = plus_time if plus_time >= 0 else minus_time
    # print("go_time", go_time)

    # 새로운 가이드의 원점과 시간
    guide_position = [trav_x + trav_velocity * cos(trav_angle) * go_time, trav_y + trav_velocity * sin(trav_angle) * go_time]
    time += go_time
    # print("traveler", traveler, "guide_position", guide_position, "time", time)

    # print(sqrt(guide_position[0] ** 2 + guide_position[1] ** 2) / trav_velocity)
    # 손님 원점에 도착하는 시간
    traveler_arrival_time = time + sqrt(guide_position[0] ** 2 + guide_position[1] ** 2) / trav_velocity
    go_back_times[traveler] = traveler_arrival_time
    # if traveler_arrival_time > last_arrival_time:
    #     last_arrival_time = traveler_arrival_time


N_travelers = int(input())
guide_velocity = float(input())
information_travelers = [0] * N_travelers
for i in range(N_travelers):
    information_travelers[i] = list(map(float, input().split()))

# print(guide_velocity)
# for i in information_travelers:
#     print(i)

guide_position = [0, 0]
nums = list(range(N_travelers))
time = 0
go_back_times = [0] * N_travelers
last_arrival_time = 0
min_go_back_times = [0] * N_travelers
min_last_arrival_time = 10000000000000


# 순열
perm(N_travelers, 0)

# print(go_back_times)
# print(min_last_arrival_time)
print(round(min_last_arrival_time))
# print(ceil(min_last_arrival_time))

