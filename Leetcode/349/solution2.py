class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        result = []
        
        for num in nums1:
            if num not in dic1:
                dic1[num] = 1
        
        for num in nums2:
            if num in dic1 and dic1[num]:
                result.append(num)
                dic1[num] -= 1

        return result