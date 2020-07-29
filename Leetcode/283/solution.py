class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        N = len(nums)
        for i in range(N):
            if nums[i] == 0:
                zero_count += 1
            elif zero_count != 0:
                swap_idx = i - zero_count
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
