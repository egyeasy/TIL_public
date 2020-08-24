class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr_idx = len(digits) - 1
        added = 1
        
        while curr_idx >= 0 and added:
            num = digits[curr_idx]
            added = (num + 1) // 10
            digits[curr_idx] = (num + 1) % 10
            
            curr_idx -= 1
            
        if added:
            digits.insert(0, 1)
        
        return digits