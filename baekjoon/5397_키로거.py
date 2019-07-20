# import sys
# sys.stdin = open('./5397.txt', 'r')

class Number:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

T = int(input())
for tc in range(T):
    first = Number()
    first.next = first
    first.prev = first
    cursor = first

    commands = input()
    for comm in commands:
        if comm == '<':
            if cursor != first:
                cursor = cursor.prev
        elif comm == '>':
            if cursor != first:
                cursor = cursor.next
        elif comm == '-':
            if cursor != first:
                cursor.next.prev = cursor.prev
                cursor.prev.next = cursor.next
                cursor = cursor.prev
        else:
            cursor.next = Number(comm, cursor, cursor.next)
            cursor.next.next.prev = cursor.next
            cursor = cursor.next

    print_cursor = first.next
    while print_cursor != first:
        print(print_cursor.value, end="")
        print_cursor = print_cursor.next