order_dict = {}

def compare(word1, word2):
    global order_dict
    len1 = len(word1)
    len2 = len(word2)
    min_len = len1 if len1 < len2 else len2
    for i in range(min_len):
        order1 = order_dict[word1[i]]
        order2 = order_dict[word2[i]]
        if order1 > order2:
            return False
        elif order1 < order2:
            return True
    if len1 > len2:
        return False
    else:
        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        global order_dict
        N = len(words)
        if N <= 1:
            return True
        
        order_dict = {}
        count = 0
        for al in order:
            order_dict[al] = count
            count += 1
        
        for i in range(1, N):
            if not compare(words[i - 1], words[i]):
                return False
        
        return True