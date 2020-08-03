class Solution:
    def decodeString(self, s: str) -> str:
        word_stack = [""]
        num_stack = []
        single_num_stack = ""
        nums = [str(_) for _ in range(10)]
        
        for let in s:
            if let in nums:
                single_num_stack += let
            elif let == "[":
                word_stack.append("")
                num_stack.append(int(single_num_stack))
                single_num_stack = ""
            elif let == "]":
                if num_stack:
                    multiply = num_stack.pop()
                else:
                    multiply = 1
                new_word = multiply * word_stack.pop()
                if word_stack:
                    word_stack[-1] += new_word
                else:
                    word_stack.append(new_word)
            else:
                word_stack[-1] += let
        
        return word_stack[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))
    print(sol.decodeString("abc3[cd]xyz"))
    print(sol.decodeString("3[a]2[b4[F]c]"))
    print(sol.decodeString(""))
    
