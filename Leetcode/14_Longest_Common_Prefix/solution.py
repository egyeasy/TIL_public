# 1. 2분탐색
# 2. sort하고 짧은거 기준으로 검색 하기

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        idx = 0
        while True:
            go_out = False
            if not strs:
                return answer
            
            for word in strs:
                if len(word) > 0:
                    prefix_cand = strs[0][idx]
                    break
            else:
                return answer
            
            for word in strs:
                if len(word) < idx + 1 or word[idx] != prefix_cand:
                    go_out = True
                    break
                
            if go_out:
                break
            
            answer += prefix_cand
            idx += 1

        return answer

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
    print(solution.longestCommonPrefix([""]))
