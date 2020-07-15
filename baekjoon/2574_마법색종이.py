import sys
sys.stdin = open("2574.txt", "r")

import copy

min_square = 10000000000
max_square = 0

class Node:
    def __init__(self, leftdown, rightup, is_white):
        self.leftdown_ = leftdown
        self.rightup_ = rightup
        self.is_white_ = is_white
    
    def collideWith(self, x, y):
        return not (x < self.leftdown_[0] or x > self.rightup_[0] or \
                    y < self.leftdown_[1] or y > self.rightup_[1])
    
    def getSquare(self):
        return abs(self.leftdown_[0] - self.rightup_[0]) * abs(self.leftdown_[1] - self.rightup_[1])

nodes = [0] * 60100
node_count = 1
M_x, N_y = map(int, input().split())
K = int(input())
head_node = Node([0, 0], [M_x, N_y], True)
nodes[0] = head_node

for i in range(K):
    x, y = map(int, input().split())
    i = 0
    for i in range(node_count):
        node = nodes[i]
        if node.collideWith(x, y):
            parent_node = node
            break
    
    node1 = copy.deepcopy(parent_node)
    node2 = copy.deepcopy(parent_node)

    if parent_node.is_white_:
        node1.leftdown_[1] = y
        node2.rightup_[1] = y
        node1.is_white_ = False
        node2.is_white_ = False
    else:
        node1.leftdown_[0] = x
        node2.rightup_[0] = x
        node1.is_white_ = True
        node2.is_white_ = True
    
    nodes[i] = node1
    nodes[node_count] = node2
    node_count += 1

for i in range(node_count):
    square = nodes[i].getSquare()
    if square > max_square:
        max_square = square
    if square < min_square:
        min_square = square

print(max_square, min_square)
