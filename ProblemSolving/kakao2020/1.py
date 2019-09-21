s = "abababcabc"

def go(word, leng, result_lengths, total_len):
    i = 0
    while i + leng <= total_len:
        standard = word[i:i+leng]
        if word[i+leng:i+2*leng] == standard:
            result_lengths[leng] += leng + 1
            while i+leng <= total_len and word[i:i+leng] == standard:
                i += leng
        else:
            result_lengths[leng] += leng
            i += leng
    result_lengths[leng] += len(word[i:])

def solution(s):
    total_len = len(s)
    lengths = [0] * (total_len + 1)
    for length in range(1, total_len + 1):
        go(s, length, lengths, total_len)
        # print()
    answer = min(lengths[1:])
    print(lengths)
    print(answer)
    return answer


solution(s)