# 15강: 환형 큐 (Circular Queue)

### 큐의 활용

- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로(asynchronously) 일어나는 경우
- 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
- 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
- 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우



### 환형 큐(Circular Queue)

정해진 개수의 저장 공간을 빙 돌려가며 이용

큐가 가득 차면? -> 더 이상 원소를 넣을 수 없음(큐 길이를 기억하고 있어야)



### 새롭게 추가된 연산

`isFull()` - 큐에 데이터 원소가 꽉 차 있는지를 판단

`front` - pop()을 시행하고 난 자리의 인덱스

`rear` - push()를 시행할 자리 인덱스





# 15강 실습: 환형 큐 구현

Python 의 내장 데이터형인 리스트 (list) 를 이용하여 환형 큐의 추상적 자료 구조를 구현한 클래스 `CircularQueue` 를 완성하세요.

```python
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.front + self.count + 1) % self.maxCount # 빈 칸
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty(): # 빈 칸
            raise IndexError('Queue empty')
        self.front = (self.rear - self.count + 1) % self.maxCount # 빈 칸
        x = (self.data[:self.front] + [None] + self.data[self.front:]).pop(self.front+1) # 빈 칸
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount] # 빈 칸



def solution(x):
    return 0
```

=> 나머지 연산을 활용한 환형 인덱싱이 주요 포인트였던 것 같다. 그리고 dequeue에서 self.data를 처리함과 동시에 pop된 x값을 반환하는 코드를 짜는 데 고민이 좀 필요했다.

