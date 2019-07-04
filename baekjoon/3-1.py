import sys
sys.stdin = open('3.txt','r')

def calculate_maxpal(word, index, total_length):
    max_length = 1
    gap = 1
    pal_possible = True
    while 0 <= index - gap and index + gap < total_length:
        if word[index - gap] == word[index + gap]:
            max_length += 2
            gap += 1
        else:
            pal_possible = False
            return pal_possible
    if index - gap < 0:
        
    return max_length

N = int(input())
for tc in range(N):
    s = input()

    answer = 0

    total_len = len(s)
    for idx in range(total_len):
        idx_max_length = calculate_added(s, idx, total_len)
        print(idx, idx_max_length)
        if idx_max_length > answer:
            if idx_max_length == total_len:
                answer = idx_max_length
                break
            answer = idx_max_length
    print(answer)
        