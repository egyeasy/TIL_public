def check(query, word):
    len_query = len(query)
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
    len_word = len(words)
    answer = [0] * len_query
    words.sort(key=lambda x: len(x))
    len_index_dict = {}
    max_len = len(words[-1])
    min_len = len(words[0])
    
    for i in range(len_word - 1, -1, -1):
        word = words[i]
        len_index_dict[len(word)] = i
    print(max_len, min_len, len_index_dict)
    
    for i in range(len_query):
        query = queries[i]
        leng = len(query)
        if leng > max_len or leng < min_len:
            continue
        start = len_index_dict[leng]
        if leng + 1 <= max_len:
            end = len_index_dict[leng + 1] 
        else:
            end = len_word
        for j in range(start, end):
            word = words[j]
            if check(query, word):
                answer[i] += 1
            
    return answer

print(solution(["a" * 1000 for _ in range(10000)], ["?" * 1000 for _ in range(10000)]))