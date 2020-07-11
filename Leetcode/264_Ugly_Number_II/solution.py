class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        idx_2, idx_3, idx_5 = 0, 0, 0
        nums.append(1)
        for i in range(1, n):
            min_value = min(2 * nums[idx_2], min(3 * nums[idx_3], 5 * nums[idx_5]))
            if min_value == 2 * nums[idx_2]:
                idx_2 += 1
            elif min_value == 3 * nums[idx_3]:
                idx_3 += 1
            else:
                idx_5 += 1
            nums.append(min_value)
        return nums[n - 1]

