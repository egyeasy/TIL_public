import sys
sys.stdin = open('2635.txt', 'r')

# binary search to find 2nd value




# make_list function to make a sequence and get the length

N = int(input())
max_cnt = 0
max_lists = []
for i in range(N // 2, N + 1):
        cnt = 2
        lists = [N, i]
        value = N - i
        while value >= 0:
            lists.append(value)
            cnt += 1
            former = i
            i = value
            value = former - i
        if cnt >= max_cnt:
            max_cnt = cnt
            max_lists = lists

print(max_cnt)
for i in max_lists:
    print(i, end=" ")
print()


