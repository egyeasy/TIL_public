# time limit exceeded : search all numbers
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [0] * (n + 1)
        i = 0
        num = 1
        while i < n + 1:
            origin_num = num

            while not num % 5:
                num //= 5

            while not num % 3:
                num //= 3

            while not num % 2:
                num //= 2

            if num == 1:
                uglies[i] = origin_num
                i += 1
                # print(uglies)
            num = origin_num + 1

        return uglies[n - 1]
