# food_times = [3, 1, 2]
# k = 5
food_times = [1, 1, 1]
k = 3

def solution(food_times, k):
    count = 0
    len_total = len(food_times)
    
    summ = -1
    found = False
    answer = -1
    while summ:
        summ = 0
        for i in range(len_total):
            if food_times[i] > 0:
                count += 1
                food_times[i] -= 1
                summ += food_times[i]
            if count == k + 1:
                found = True
                answer = i + 1
                break
            print("nums:", food_times)
        if summ == 0:
            break
        if found == True:
            break
    print(answer)

    return answer


    

solution(food_times, k)