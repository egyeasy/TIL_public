import sys
sys.stdin = open('2669.txt', 'r')

mat = [[0] * 100 for i in range(100)]

for i in range(4):
    aline = input()
    a = list(map(int, aline[:3].split()))
    b = list(map(int, aline[4:].split()))
    # a = [100 - a[1], a[0]]
    # b = [100 - b[1], b[0]]
    # print(a, b)
    for alist in mat[a[0]:b[0]]:
        for i in range(100):
            if a[1] <= i and i < b[1]:
                alist[i] = 1
    # for i in range(100):
    #     if b[0] <= i < a[0]:
    #         for j in range(100):
                

# for i in mat:
#     print(i)
total_sum = 0
for aline in mat:
    total_sum += sum(aline)

print(total_sum)