food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    index = 0
    len_total = len(food_times)
    
    div_total = k // len_total
    remain_total = k % len_total

    print(div_total, remain_total)
    
    # 번호 수 == 최종 배열 자릿수로 할 것
    index = remain_total

    for i in range(len_total):
        if food_times[i] < div_total:
            index = index + div_total - food_times[i]
            if i <= remain_total:
                index += 1
            # index %= len_total
            print(i, index)
        elif food_times[i] == div_total:
            if i <= remain_total:
                index += 1
            # index %= len_total
            print(i, index, "같을 때")
    index %= len_total
    print(index + 1)
    return index + 1

solution(food_times, k)