class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        elif num <= 0:
            return False

        while not num % 5:
            num //= 5
        
        while not num % 3:
            num //= 3
        
        while not num % 2:
            num //= 2

        return num == 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))