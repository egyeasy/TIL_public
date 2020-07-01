from collections import deque

par_map = {')': '(', '}': '{', ']': '['}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for letter in s:
            if letter not in par_map:
                stack.append(letter)
            else:
                if not stack:
                    return False
                elif stack[-1] == par_map[letter]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("{[]}"))
    print(solution.isValid("{"))