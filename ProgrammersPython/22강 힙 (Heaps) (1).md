# 22강: 힙 (Heaps)



### 힙이란?

이진 트리의 한 종류 (이진 힙 - binary heap)

1. 루트 (root) 노드가 언제나 최댓값 또는 최솟값을 가짐
   - 최대 힙(max heap), 최소 힙(min heap)
2. 완전 이진 트리여야 함



### 최대 힙의 예

재귀적으로도 정의됨(어느 노드를 루트로 하는 서브트리도 모두 최대 힙)



### 이진 탐색 트리와의 비교

1. 원소들은 완전히 크기 순으로 정렬되어 있는가? NO
2. 특정 키 값을 가지는 원소를 빠르게 검색할 수 있는가? NO
3. 부가의 제약 조건은 어떤 것인가? 완전 이진 트리여야 한다.



### 최대 힙(Max heap)의 추상적 자료구조

연산의 정의

- `__init__()` : 빈 최대 힙을 생성
- insert(item) : 새로운 원소를 삽입
- remove() : 최대 원소 (root node) 를 반환(그리고 동시에 이 노드를 삭제)



### 데이터 표현의 설계

배열을 이용한 이진 트리의 표현

노드 번호 m을 기준으로

- 왼쪽 자식의 번호: 2 * m
- 오른쪽 자식의 번호: 2 * m + 1
- 부모 노드의 번호: m // 2

완전 이진트리이므로(배열로 구현하는 것이 쉽고)

- 노드의 추가/삭제는 마지막 노드에서만



### 최대 힙에 원소 삽입

1. 트리의 마지막 자리에 새로운 원소를 임시로 저장
2. 부모 노드와 키 값을 비교하여 부모보다 큰 값이라면 위로, 위로, (부모 노드와 자리를 바꿔가며) 이동



### 최대 힙에 원소 삽입 - 복잡도

원소의 개수가 n인 최대 힙에 새로운 원소 삽입

-> 부모 노드와의 대소 비교 최대 횟수 : log2n

최악 복잡도O(log n)의 삽입 연산





# 22강 실습: 최대 힙에 새로운 원소 삽입

```python
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        the_idx = len(self.data) - 1
        par_idx = the_idx // 2
        while par_idx != 0:
            if self.data[the_idx] > self.data[par_idx]:
                self.data[the_idx], self.data[par_idx] = self.data[par_idx], self.data[the_idx]
                the_idx = par_idx
                par_idx = the_idx // 2
            else:
                break


def solution(x):
    return 0
```

무한 루프에 걸리면 while문에 탈출 경로가 있는지 즉각적으로 확인해볼 것.