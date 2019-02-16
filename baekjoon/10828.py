"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

> input
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

> output
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

7
pop
top
push 123
top
pop
top
pop

"""


T = int(input())

stack = [0] * T
top_ = -1

def push(item):
    global top_
    stack[top_ + 1] = item
    top_ += 1
    
def pop():
    global top_
    if top_ == -1:
        return -1
    pop_item = stack[top_]
    stack[top_] = 0
    top_ -= 1
    return pop_item

def size():
    global top_
    return top_ + 1

def empty():
    global top_
    return int(top_ == -1)

def top():
    global top_
    if top_ == -1:
        return -1
    return stack[top_]


for tc in range(1, T + 1):
    command = input().split()

    if len(command) > 1:
        push(int(command[1]))
    else:
        command = command[0]
        if command == 'pop':
            print(pop())
        elif command == 'size':
            print(size())
        elif command == 'empty':
            print(empty())
        else:
            print(top())

# idea
# 1. Thought the size of stack doesen't matter and really it wasn't in the example cases.
# but it mattered in test. 