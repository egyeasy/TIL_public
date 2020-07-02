class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        have_to_break = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if have_to_break:
                    break
            else:
                have_to_break = True
                count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("hi  "))
    print(solution.lengthOfLastWord("hi hii "))
    print(solution.lengthOfLastWord(""))
    print(solution.lengthOfLastWord(" "))
