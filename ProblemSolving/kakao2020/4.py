# 2020.01.15 정확성 OK, 효율성 Not OK
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