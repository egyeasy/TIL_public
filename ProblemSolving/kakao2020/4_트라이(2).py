# 트라이 구현 참고
# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

from collections import deque
count = 0

def backtrack(node, len_question, depth):
    global count
    if len_question == depth:
        if node.data:
            count += 1
        return
    for child in node.children.values():
        backtrack(child, len_question, depth + 1)

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
    def starts_with(self, prefix, len_question):
        global count
        result = 0
        curr_node = self.head
        subtrie = curr_node

        # 트라이에서 prefix를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return result
        
        # bfs로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())
        
        while queue:
            curr = queue.pop()
            if curr.data != None:
                if len(curr.data) == len_query:
                    result += 1
            elif len(curr.data) < len_query:
                queue += list(curr.children.values())
        
        return result



def solution(words, queries):
    len_query = len(queries)
    answer = [0] * len_query
    tries = [Trie() for _ in range(10001)]
    r_tries = [Trie() for _ in range(10001)]

    for word in words:
        tries[len(word)].insert(word)
        r_tries[len(word)].insert(word[::-1])

    for i in range(len_query):
        query = queries[i]
        if query[-1] == "?":
            prefix = query.split("?")[0]
            answer[i] = tries[len(query)].starts_with(prefix, len(query) - len(prefix))
        else:
            reversed_query = query[::-1]
            prefix = reversed_query.split("?")[0]
            answer[i] = r_tries[len(query)].starts_with(prefix, len(query) - len(prefix))
        
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                ["fro??", "????o", "fr???", "fro???", "pro?"]))