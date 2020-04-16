result = []

def judge(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    
    if len1 != len2:
        return False
    
    for i in range(len1):
        if word2[i] == '*':
            continue
        elif word1[i] != word2[i]:
            return False
        
    return True

def backtrack(user_id, banned_id, visited_u, visited_b, len_u, len_b):
    
    if sum(visited_b) == len_b:
        result.append(str(visited_u))
    
    for i in range(len_b):
        if not visited_b[i]:
            for j in range(len_u):
                if not visited_u[j] and judge(user_id[j], banned_id[i]):
                    visited_u[j] = 1
                    visited_b[i] = 1
                    backtrack(user_id, banned_id, visited_u, visited_b, len_u, len_b)
                    visited_u[j] = 0
                    visited_b[i] = 0
                    
        

def solution(user_id, banned_id):
    
    u_len = len(user_id)
    b_len = len(banned_id)
    
    if u_len == b_len:
        return 1
    
    visited_u = [0] * u_len
    visited_b = [0] * b_len
    
    backtrack(user_id, banned_id, visited_u, visited_b, u_len, b_len)
    
    total_result = []
    for i in result:
        if not i in total_result:
            total_result.append(i)
    
    return len(total_result)