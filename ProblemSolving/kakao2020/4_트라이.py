# 2020.08.06 동훈 솔루션 보고 다시

class Node:
    def __init__(self, char):
        self.char = char
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        curr_node = self.head
        for c in word:
            if c in curr_node.children.keys():
                curr_node = curr_node.children[c]
            else:
                curr_node.children[c] = Node(c)
                curr_node = curr_node.children[c]
            curr_node.count += 1
    
    def search(self, prefix):
        curr_node = self.head
        for c in prefix:
            if not c in curr_node.children.keys():
                return 0
            curr_node = curr_node.children[c]
        return curr_node.count
        
    
def solution(words, queries):
    tries = [Trie() for _ in range(10001)]
    r_tries = [Trie() for _ in range(10001)]
    answer = [0] * len(queries)
    for word in words:
        tries[len(word)].insert(word)
        r_tries[len(word)].insert(word[::-1])
    
    for i, query in enumerate(queries):
        if query[-1] == "?":
            answer[i] = tries[len(query)].search(query.split("?")[0])
        else:
            answer[i] = r_tries[len(query)].search(query.split("?")[-1][::-1])
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
print(solution(["abcc", "a", "ab", "abccd"], ["?"]))
print(solution(["fff", "fer", "ffef", "fsrrere"], ["?", "???", "f??", "??????e", "?????????", "efkejflewjfe?", "????fejfoiewfj"]))
print(solution(["f", "fr"], ["?", "f?"]))
