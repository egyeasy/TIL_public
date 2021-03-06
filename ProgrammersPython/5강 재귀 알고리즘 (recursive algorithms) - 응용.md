# 5강: 재귀 알고리즘 (recursive algorithms) - 응용

얼핏 생각하는 것보다 많은 문제들이 재귀적인 방법으로 풀어집니다. 여기에서는, 아래와 같은 문제들을 재귀 알고리즘으로 풀어보겠습니다.

- 조합의 수 (n 개의 서로 다른 원소에서 m 개를 택하는 경우의 수) 구하기
- 하노이의 탑 (크기 순서로 쌓여 있는 원반을 한 막대에서 다른 막대로 옮기기)
- 피보나치 순열

문제의 종류에 따라서는 재귀 알고리즘을 적용함으로써 알고리즘을 간단하고 이해하기 쉽게 서술할 수 있다는 장점이 있습니다. 그런데, 문제를 풀어 내는 데 걸리는 시간 측면에서는 어떨까요?

하나의 재귀 알고리즘이 주어질 때, 이것을 재귀적이지 않은 (non-recursive) 방법으로 동일하게 풀어내는 알고리즘이 존재한다는 것을 수학적으로 증명할 수 있습니다. 보통은 순환문 (loop) 을 이용해서 정해진 연산을 반복함으로써 문제의 답을 구하는데, 따라서 반복적 (iterative) 알고리즘이라고 부르기도 합니다. 일반적으로, 주어진 문제에 대해서 반복적인 알고리즘이 재귀적인 알고리즘보다 문제 풀이의 (시간적) 효율이 높습니다.

그럼에도 불구하고, 재귀 알고리즘이 가지는 특성 때문에 트리 (tree) 와 같은 - 제 17 강에서 등장하게 됩니다 - 자료 구조를 이용하는 알고리즘에는 매우 직관적으로 적용할 수 있는 경우가 많습니다. 이 강의에서는 이진 탐색 (binary search) 알고리즘을 재귀적으로 구현하는 빈 칸 채우기 코딩 연습문제를 풀어보기로 합시다.



### 조합의 수 계산

```python
from math import factorial as f

def combi(n, m):
    return f(n)/(f(m)*f(n-m))
```



### 조합의 수 계산 - 재귀적 방법으로

``` python
def combi(n, m):
    # 예외적 케이스 처리 -> 점화식 내에서 (n-1 < m)이 나오거나 (m-1 < 0)이 나오지 않도록!
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)
```

재귀함수의 경우 중복해서 호출하는 함수가 존재해서 비효율적인 경우들이 있다.



# 5강 실습: 재귀적 이진 탐색 구현하기

리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어지고, 또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l 부터 u 까지로 (인자로) 정해질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

인덱스 범위를 나타내는 l 과 u 가 인자로 주어지는 이유는, 이 함수를 재귀적인 방법으로 구현하기 위함입니다. 빈 칸에 알맞은 내용을 채워서 재귀 함수인 solution() 을 완성하세요.

예를 들어,
L = [2, 3, 5, 6, 9, 11, 15]
x = 6
l = 0
u = 6
의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

또 다른 예로,
L = [2, 5, 7, 9, 11]
x = 4
l = 0
u = 4
로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.



# 5강 실습: 재귀적 이진 탐색 구현하기

```python
def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, mid + 1, u)
```

