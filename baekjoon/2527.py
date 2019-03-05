import sys
sys.stdin = open('2527.txt', 'r')

for i in range(4):
    aline = list(map(int, input().split()))
    M = max(aline)
    a1 = aline[:2]
    a2 = aline[2:4]
    b1 = aline[4:6]
    b2 = aline[6:]
    # print(a1, a2, b1, b2)
    
    if a1[0] > b1[0]:
        a1, a2, b1, b2 = b1, b2, a1, a2
    # print(a1, a2, b1, b2)
    # print()
    # print(b1[0] - a2[0])
    # print(b1[1] - a2[1])
    # print(b2[1] - a1[1])
    x_gap = b1[0] - a2[0]
    lower_gap = b1[1] - a2[1]
    upper_gap = b2[1] - a1[1]
    # print()
    # result = "d"
    if x_gap > 0:
        result = "d"
    elif x_gap == 0:
        if lower_gap == 0 or upper_gap == 0:
            result = "c"
        elif lower_gap < 0 and upper_gap > 0:
            result = "b"
    else:
        if lower_gap > 0 or upper_gap < 0:
            result = "d"
        elif lower_gap == 0 or upper_gap == 0:
            result = "b"
        else:
            result = "a"
    print(result)
    # print()