import sys
sys.stdin = open('2.txt','r')

def calculate_maxpal(word, index, total_length):
    max_length = 1
    gap = 1
    while 0 <= index - gap and index + gap < total_length:
        if word[index - gap] == word[index + gap]:
            max_length += 2
        gap += 1
    return max_length

def solution(s):
    answer = 0

    total_len = len(s)
    for idx in range(total_len):
        idx_max_length = calculate_maxpal(s, idx, total_len)
        if idx_max_length > answer:
            if idx_max_length == total_len:
                return idx_max_length
            answer = idx_max_length
            
    return answer