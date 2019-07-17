N = int(input())

move_list = []
move_count = 0
def move_hanoi(n, start, middle, end):
    global move_count
    if n == 0:
        return
    move_hanoi(n - 1, start, end, middle)
    move_list.append("{} {}".format(start, end))
    move_count += 1
    move_hanoi(n - 1, middle, start, end)

move_hanoi(N, 1, 2, 3)
print(move_count)
for move in move_list:
    print(move)