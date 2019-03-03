# input의 좌우 바뀌면 결과가 다르게 나옴
import sys
sys.stdin = open('2650.txt', 'r')

num_points = int(input())
num_lines = num_points // 2
lists = [[] for _ in range(5)]
dicts = {}

result = 0
max_cnt = 0

for i in range(num_lines):
    cnt = 0
    aline = list(map(int, input().split()))
    a = tuple(aline[:2])
    b = tuple(aline[2:])
    print(a, b)
    if a[0] == b[0]:
        maxx = max(a[1], b[1])
        minn = min(a[1], b[1])
        for i in range(minn + 1, maxx):
            if i in lists[a[0]]:
                if dicts[(a[0], i)][0] != a[0]:
                    cnt += 1
                else:
                    if dicts[(a[0], i)][1] > maxx or dicts[(a[0], i)][1] < minn:
                        cnt += 1
    elif sorted([a[0], b[0]]) in [[1, 3], [1, 4], [2, 4], [2, 3]]:
        print(f"구석: {a}, {b}")
        for i in range(1, a[1]):
            if i in lists[a[0]]:
                print(f"{a[0]}, {i}")
                other = dicts[(a[0], i)]
                if other[0] == a[0] and other[1] > a[1]:
                    cnt += 1
                elif other[0] == b[0] and other[1] > b[1]:
                    cnt += 1
                else:
                    cnt += 1
        for i in range(1, b[1]):
            if i in lists[b[0]]:
                other = dicts[(b[0], i)]
                if other[0] == b[0] and other[1] > b[1]:
                    cnt += 1
                elif other[0] == a[0] and other[1] > a[1]:
                    cnt += 1
                else:
                    cnt += 1
    else:
        if sorted([a[0], b[0]]) == [1, 2]:
            for i in range(1, a[1]):
                if i in lists[a[0]]:
                    other = dicts[(a[0], i)]
                    if other[0] == 4:
                        cnt += 1
                    elif other[0] == a[0] and other[1] > a[1]:
                        cnt += 1
                    elif other[0] == b[0] and other[1] > b[1]:
                        cnt += 1
            for i in range(1, b[1]):
                if i in lists[b[0]]:
                    other = dicts[(b[0], i)]
                    if other[0] == 4:
                        cnt += 1
                    elif other[0] == a[0] and other[1] > a[1]:
                        cnt += 1
                    elif other[0] == b[0] and other[1] > b[1]:
                        cnt += 1
            for i in lists[3]:
                other = dicts[(3, i)]
                if other[0] == 4:
                    cnt += 1
                elif other[0] == a[0] and other[1] > a[1]:
                    cnt += 1
                elif other[0] == b[0] and other[1] > b[1]:
                    cnt += 1
        if sorted([a[0], b[0]]) == [3, 4]:
            for i in range(1, a[1]):
                if i in lists[a[0]]:
                    other = dicts[(a[0], i)]
                    if other[0] == 4:
                        cnt += 1
                    elif other[0] == a[0] and other[1] > a[1]:
                        cnt += 1
                    elif other[0] == b[0] and other[1] > b[1]:
                        cnt += 1
            for i in range(1, b[1]):
                if i in lists[b[0]]:
                    other = dicts[(b[0], i)]
                    if other[0] == 4:
                        cnt += 1
                    elif other[0] == a[0] and other[1] > a[1]:
                        cnt += 1
                    elif other[0] == b[0] and other[1] > b[1]:
                        cnt += 1
            for i in lists[1]:
                other = dicts[(1, i)]
                if other[0] == 2:
                    cnt += 1
                elif other[0] == a[0] and other[1] > a[1]:
                    cnt += 1
                elif other[0] == b[0] and other[1] > b[1]:
                    cnt += 1
    print(f"cnt: {cnt}")
    result += cnt
    if cnt > max_cnt:
        max_cnt = cnt
    lists[a[0]].append(a[1])
    lists[b[0]].append(b[1])
    dicts[a] = b
    dicts[b] = a

    print()

print(result)