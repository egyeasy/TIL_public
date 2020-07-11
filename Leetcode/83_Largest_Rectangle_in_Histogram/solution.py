from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        if N == 0:
            return 0
        arr = [0] * N

        max_area = 0

        for i in range(N):
            arr[i] = heights[i]
            if arr[i] > max_area:
                max_area = arr[i]

        for ran_num in range(1, N):
            for i in range(0, N - ran_num):
                j = i + ran_num
                range_heights = heights[i : j + 1]
                total_rec = min(range_heights) * len(range_heights)
                arr[i] = max(arr[i], arr[j], total_rec)
                if arr[i] > max_area:
                    max_area = arr[i]
            # print(arr)
        return max_area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    print(solution.largestRectangleArea(heights))
