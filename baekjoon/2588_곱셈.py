first = int(input())
second = input()

summ = 0
idx = 1

for digit in second[::-1]:
    part_result = first * int(digit)
    print(part_result)
    summ += part_result * idx
    idx *= 10

print(summ)