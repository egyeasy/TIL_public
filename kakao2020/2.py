p = "(()())()"
# def push(stack, item):
#     stack.append(item)

# def pop(stack):
#     item = stack[-1]
#     del stack[-1]
#     return item

# def look(stack):
#     print("look:", stack[-1])
#     return stack[-1]

def judge(p):
    stack = []
    for ch in p:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                try:
                    stack.pop()
                except IndexError:
                    return False
    return len(stack) == 0

def judge_u(p):
    counts = {'(': 0, ')': 0}
    for i, ch in enumerate(p):
        counts[ch] += 1
        if counts['('] == counts[')']:
            return i
    return 0

def dizip(u):
    short_u = u[1:-1]
    new_word = ""
    for char in short_u:
        if char == "(":
            new_word += ")"
        else:
            new_word += "("
    return new_word
        

def recursive(p):
    if p == '':
        return ''
    else:
        idx = judge_u(p)
        print("idx:", idx)
        u = p[:idx + 1]
        v = p[idx + 1:]
        if judge(u):
            word = recursive(v)
            return u + word
        else:
            bin_word = '('
            bin_word += recursive(v)
            bin_word += ')'
            diz_u = dizip(u)
            bin_word += diz_u
            return bin_word
        


def solution(p):
    answer = recursive(p)
    # if p == '':
    #     answer = ''
    # elif judge(p):
    #     answer = p
    # else:
    #     idx = judge_u(p)
    #     print(idx)
    #     u = p[:idx + 1]
    #     v = p[idx + 1:]
    #     print("u:", u, "v:", v)
    #     # u가 올바른 괄호 문자열이라면
    #     if judge(u):
    #         pass
    #     # 아니라면
    #     else:
    #         word = "("
    #         if v == '':
    print("answer")
    print(answer)

    return answer


solution(p)