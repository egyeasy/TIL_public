import sys
sys.stdin = open('5658.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, K = map(int, input().split())
    aline = input()
    word_len = n // 4
    result = []
    # print(aline)
    for k in range(word_len):
        new_line = aline[n - k:] + aline[:n - k]
        for i in range(4):
            word = new_line[word_len*i:word_len*(i + 1)]
            if not word in result:
                result.append(word)
        # print(result)
    # print(n, K - 1)
    # print(sorted(result, reverse=True))
    # print(sorted(result, reverse=True)[K - 1])
    print("#{}".format(tc), int(sorted(result, reverse=True)[K - 1], 16))

    # print()