class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
            else:
                break

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("hi  "))
    print(solution.lengthOfLastWord("hi hii "))
    print(solution.lengthOfLastWord(""))
    print(solution.lengthOfLastWord(" "))
