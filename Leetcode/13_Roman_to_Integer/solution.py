# 예외가 되는 케이스(e.g. IV)들이 앞숫자-뒷문자의 대소 관계가 다르다는 점에 주목할 것(https://medium.com/@angelahiking/13-roman-to-integer-python-easy-cabcb1d6b8a3)

num_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
before_map = {
    "C": ["D", "M"],
    "X": ["L", "C"],
    "I": ["V", "X"],
    "M": [],
    "D": [],
    "L": [],
    "V": [],
}


class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            letter = s[i]
            if i + 1 < len(s) and num_map[letter] < num_map[s[i + 1]]:
                sum -= num_map[letter]
            else:
                sum += num_map[letter]
        return sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("LVIII"))
