import sys
sys.stdin = open("1240.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    for i in range(n):
        text = input()
    print(text)
    print(n, m)
    total_len = m // 7

    print(total_len)
    
    bin_list = [[0] * 7 for i in range(total_len)]
    print(bin_list)
    for i in range(m):
        quo = i // 7
        rem = i % 7
        print(i, quo, rem)
        print(text[i])
        bin_list[quo][rem] = text[i]

    print(bin_list)
