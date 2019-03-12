import sys
sys.stdin = open('10157.txt', 'r')

garo, sero = map(int, input().split())
target_num = int(input())

if target_num > garo * sero:
    print(0)
else:
    n = 1
    total = 0
    while total < target_num:
        total += 2 * (garo + sero - 2 * (2 * n - 1))
        n += 1
    total -= 2 * (garo + sero - 2 * (2 * (n - 1) - 1))
    n -= 1
    # print(n, total)
    point = [n, n - 1]

    new_garo = garo - 2 * (n - 1)
    new_sero = sero - 2 * (n - 1)
    found = False

    # print("total", total)

    for i in range(new_sero):
        # print(point)
        if total == target_num:
            print(point[0], point[1])
            found = True
            break
        total += 1
        point[1] += 1
    # print()
    if not found:
        for i in range(new_garo - 1):
            # print(point)
            if total == target_num:
                print(point[0], point[1])
                found = True
                break
            total += 1
            point[0] += 1

    if not found:
        for i in range(new_sero - 1):
            if total == target_num:
                print(point[0], point[1])
                found = True
                break
            total += 1
            point[1] -= 1

    if not found:
        for i in range(new_garo - 1):
            if total == target_num:
                print(point[0], point[1])
                found = True
                break
            total += 1
            point[0] -= 1


    if not found and total == target_num:
        print(point[0], point[1])

