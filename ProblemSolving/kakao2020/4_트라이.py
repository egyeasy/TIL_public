# 

# 트라이 구현 참고
# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

from collections import deque

class Node(object):

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
            # string의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string

    """
    주어진 단어 string이 트라이에 존재하는지 여부를 반환합니다.
    """
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        # string의 마지막 글자에 다다랐을 때,
        # curr_node에 data가 있다면 string이 트라이에 존재하는 것!
        if (curr_node.data != None):
            return True
        
    """
    주어진 prefix로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환합니다.
    """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # 트라이에서 prefix를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        
        # bfs로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())
        
        return result


def check(query, word):
    len_query = len(query)
    if len_query != len(word):
        return False
    if query[0] == "?":
        for i in range(len_query - 1, -1, -1):
            a = query[i]
            if a == "?":
                return True
            if a != word[i]:
                return False
    else:
        for i in range(len_query):
            a = query[i]
            if a == "?":
                return True
            if a != word[i]:
                return False
        
        

def solution(words, queries):
    len_query = len(queries)
    answer = [0] * len_query
    for i in range(len_query):
        query = queries[i]
        for word in words:
            if check(query, word):
                answer[i] += 1
            
    return answer