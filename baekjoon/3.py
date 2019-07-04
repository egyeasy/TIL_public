import sys
sys.stdin = open('3.txt','r')

def calculate_added(word, index, total_length):
    added_length = 0
    gap = 0
    pal_possible = True
    while 0 <= index - gap and index + gap < total_length:
        if word[index - gap] == word[index + gap]:
            gap += 1
        else:
            pal_possible = False
            return pal_possible, -1
    if index - gap < 0:
        added_length = total_length - (index + gap)
    elif index + gap >= total_length:
        added_length = index - gap + 1
    pal_possible = True

    return pal_possible, added_length

N = int(input())
for tc in range(N):
    s = input()
    
    answer = 0
    min_added = 10000
    is_possible = False

    total_len = len(s)
    for idx in range(total_len):
        is_possible, idx_added_length = calculate_added(s, idx, total_len)
        print(idx, idx_added_length)
        if is_possible and idx_added_length < min_added:
            if idx_added_length == 0:
                answer = total_len
                print("answer: ", answer)
            min_added = idx_added_length
    answer = total_len + min_added
    print(answer)
    print()