import sys
sys.stdin = open("2574.txt", "r")

min_square = 10000000000
max_square = 0

class Node:
    def __init__(self, leftdown, rightup, is_white):
        self.leftdown_ = leftdown
        self.rightup_ = rightup
        self.is_white_ = is_white
        self.axis_ = None
        self.left_child_ = None
        self.right_child_ = None
        self.square = abs(leftdown[0] - rightup[0]) * abs(leftdown[1] - rightup[1])
    
    def setAxis(self, axis):
        self.axis_ = axis
    
    def setChild(self, node):
        if self.left_child_:
            self.right_child_ = node
        else:
            self.left_child_ = node

def makeNode(node, x, y):
    if node.axis_:
        if node.is_white_:
            curr_axis = y
        else:
            curr_axis = x
        if curr_axis < node.axis_:
            makeNode(node.left_child_, x, y)
        else:
            makeNode(node.right_child_, x, y)
            
    else:
        if node.is_white_:
            is_white = False
            first_leftdown = node.leftdown_
            first_rightup = (node.rightup_[0], y)
            second_leftdown = (node.leftdown_[0], y)
            second_rightup = node.rightup_
            axis = y
        else:
            is_white = True
            first_leftdown = node.leftdown_
            first_rightup = (x, node.rightup_[1])
            second_leftdown = (x, node.leftdown_[1])
            second_rightup = node.rightup_
            axis = x
        first_square = abs(first_leftdown[0] - first_rightup[0]) * abs(first_leftdown[1] - first_rightup[1])
        second_square = abs(second_leftdown[0] - second_rightup[0]) * abs(second_leftdown[1] - second_rightup[1])
        
        node.setChild(Node(first_leftdown, first_rightup, is_white))
        node.setChild(Node(second_leftdown, second_rightup, is_white))
        node.setAxis(axis)

def dfs(node):
    global max_square, min_square
    if node.left_child_:
        dfs(node.left_child_)
        dfs(node.right_child_)
    else:
        if node.square > max_square:
            max_square = node.square
        if node.square < min_square:
            min_square = node.square


M_x, N_y = map(int, input().split())
K = int(input())
head_node = Node((0, 0), (M_x, N_y), True)

for i in range(K):
    x, y = map(int, input().split())
    makeNode(head_node, x, y)

dfs(head_node)

print(max_square, min_square)
