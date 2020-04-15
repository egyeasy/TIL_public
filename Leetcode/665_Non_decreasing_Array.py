class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        leng = len(nums)
        if leng == 1 | leng == 2:
            return True
        is_changed = False
        for i in range(1, leng - 1):
            if nums[i-1] > nums[i]:
                if is_changed:
                    return False
                if nums[i] > nums[i+1]:
                    return False
                elif nums[i] <= nums[i+1] and nums[i-1] > nums[i+1]:
                    if i-2 >= 0 and nums[i-2] > nums[i]:
                        return False
                    nums[i-1] = nums[i]
                    is_changed = True
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                    is_changed = True
        if nums[leng-2] > nums[leng-1] and is_changed:
            return False
        return True