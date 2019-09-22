# import sys
# sys.stdin = open('4.txt', 'r')


def check(idx):
    global max_distance

    front_idx = idx
    curr_front = 0
    front_dis = -1
    front_ended = False

    rear_idx = idx
    curr_rear = 0
    rear_dis = -1
    rear_ended = False

    while not (front_ended and rear_ended):
        if not front_ended and front_idx - 1 > -1:
            front_idx -= 1
            curr_front += 1
            if nums[front_idx]:
                front_dis = curr_front
                front_ended = True
        else:
            front_ended = True

        if not rear_ended and rear_idx + 1 < N:
            rear_idx += 1
            curr_rear += 1
            if nums[rear_idx]:
                rear_dis = curr_rear
                rear_ended = True
        else:
            rear_ended = True
    
    if front_dis == -1:
        return rear_dis
    elif rear_dis == -1:
        return front_dis
    else:
        return front_dis if front_dis <= rear_dis else rear_dis
        
        

N = int(input())
nums = list(map(int, input().split()))

max_distance = -1

for i in range(N):
    if not nums[i]:
        curr_dis = check(i)
        if curr_dis > max_distance:
            max_distance = curr_dis

print(max_distance)