import sys
sys.stdin = open('12026.txt', 'r')


def dynamic(n):
    if n <= 1:
        return 0
    value = 0
    dis = 1
    while n - dis > 0:
        if word[n - dis] == dic[word[n]]:
            value = dynamic(n - dis)
            if dp[n] == -1:
                dp[n] = value + dis ** 2
            else:
                if dp[n] > value + dis ** 2:
                    dp[n] = value + dis ** 2
        dis += 1
    print(n, dp[n])
    return dp[n]
N = int(input())
word = '0' + input()

dp = [-1] * (N + 1)
dic = {
    'B': 'J',
    'O': 'B',
    'J': 'O'
}

dynamic(N)

print(dp[N])
