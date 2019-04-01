n = int(input())
s = input()
d = [-1] * n

def get_next(char):
    # 이전 word 반환
    return 0 

def go(index):
    if index == n - 1:
        return 0
    if d[index] != -1:
        return d[index]
    ans = 0
    for j in range(index + 1, n):
        if s[j] == get_next(s[index]):
            temp = go(j)
            if temp != -1:
                val = (j - index) ** 2 +temp
                if ans == -1 or ans > val:
                    ans = val
    d[index] = ans
    return ans
print(go(0))

