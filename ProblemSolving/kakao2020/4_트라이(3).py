# 2020.08.06 동훈 솔루션 보고 다시

class Node:
    def __init__(self, char):
        self.char = char
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)kkj

    def insert(word):
        curr_node = self.head
        for c in word:
            if c in curr_node.children.keys():
                curr_node = curr_node.children[c]
            else:
                curr_node.children[c] = Node(c)
                curr_node = curr_node.children[c]
            curr_node.count += 1
    

    
        

def solution(words, queries):
    