class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        origin_x = x    
        paled_num = 0
        exp = 0
        divided = 10 ** exp
    
        while x // divided > 0:
            exp += 1
            divided = 10 ** exp
        
        len_of_num = exp
        
        for i in range(len_of_num - 1, -1, -1):
            divided_by = 10 ** i
            added_num = (x // divided_by) * 10 ** (len_of_num - i - 1)
            paled_num += added_num
            x = x % divided_by
        
        print(paled_num, origin_x)
        if origin_x == paled_num:
            return True
        else:
            return False
        
if __name__ == "__main__":
    num = 1234
    s = Solution()
    print(s.isPalindrome(num))