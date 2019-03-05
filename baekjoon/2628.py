import sys
sys.stdin = open('2628.txt', 'r')

width, height = map(int, input().split())
N = int(input())
garos = [0]
seros = [0]
for i in range(N):
    sero, num = map(int, input().split())
    if sero:
        seros.append(num)
    else:
        garos.append(num)

garos.sort()
seros.sort()
garos.append(height)
seros.append(width)
# print(garos)
# print(seros)

max_area = 0
garo_len = len(garos)
sero_len = len(seros)
for i in range(garo_len):
    if i:
        for j in range(sero_len):
            if j:
                area = (garos[i] - garos[i - 1]) * (seros[j] - seros[j - 1])
                # print(garos[i], seros[j], area)
                if area > max_area:
                    max_area = area

print(max_area)
