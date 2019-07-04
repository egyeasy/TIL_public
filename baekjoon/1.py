import sys
sys.stdin = open('1.txt','r')

def judge_pal(an_int):
    is_pal = True
    an_word = str(an_int)
    total_length = len(an_word)
    half_length = total_length // 2
    for idx in range(half_length):
        if an_word[idx] != an_word[total_length - idx - 1]:
            is_pal = False
            return is_pal
    return is_pal
        
def solution(n,m):
    answer = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for num in range(n, m + 1):
        if judge_pal(num):
            answer += 1

    return answer