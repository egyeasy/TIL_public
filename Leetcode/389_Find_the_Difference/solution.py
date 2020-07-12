class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = ""
        
        s_dict = {}        
        t_dict = {}
        
        for i in range(97, 123):
            s_dict[chr(i)] = 0
            t_dict[chr(i)] = 0
        
        for letter in s:
            s_dict[letter] += 1
        
        for letter in t:
            t_dict[letter] += 1
        
        for letter in s_dict:
            if s_dict[letter] != t_dict[letter]:
                answer = letter
                return answer
        
        return answer