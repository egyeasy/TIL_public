# 17강 트리 (Trees)

정점(node)과 간선(edge)을 이용하여 데이터의 배치 형태를 추상화한 자ㄹ료구조

뿌리(root) - 제일 위

이파리(leaf) - 제일 아래

뿌리가 위에 있고 이파리가 아래 있는 거꾸로 된 구조가 일반적

내부 노드(internal node) - 뿌리도 이파리도 아닌 노드



### 노드의 수준(level)

루트 노드가 level 0. 아래 층으로 갈수록 level이 하나씩 커짐



### 트리의 높이(height)

트리의 높이 = 최대 level + 1



### 노드의 차수(degree)

= 자식(서브트리)의 수

parent 노드는 무조건 하나다!



### 이진 트리 (Binary tree)

모든 노드의 차수가 2 이하인 트리

**재귀적으로 정의할 수 있음** : 빈 트리(empty tree)이거나(무한 재귀 막기 위함) 루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리



### 포화 이진 트리(Full binary tree)

모든레벨에서 노드들이 모두 채워져 있는 이진 트리

(높이가 k이고 노드의 개수가 (2**k) - 1인 이진 트리)



### 완전 이진 트리(Complete binary tree)

높이 k인 완전 이진 트리

레벨 k-2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리

레벨 k-1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리