from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        if not strs:
            return answer

        min_word = -1
        for word in strs:
            if min_word == -1:
                min_word = word
            elif len(word) < len(min_word):
                min_word = word

        found = False
        answer_idx = 0

        for i in range(len(min_word) + 1):
            for word in strs:
                if not word.startswith(min_word[:i]):
                    answer_idx = i - 1
                    found = True
                    break
            else:
                answer_idx = i
            if found:
                break
        answer = min_word[:answer_idx]
        return answer
        


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
    print(solution.longestCommonPrefix([""]))
    print(solution.longestCommonPrefix(["a"]))
    print(solution.longestCommonPrefix(["aa", "aa"]))