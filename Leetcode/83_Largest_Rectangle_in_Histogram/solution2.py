from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        if N == 0:
            return 0
        mat = [[0] * N for _ in range(N)]

        for i in range(N):
            mat[i][i] = heights[i]

        for ran_num in range(1, N):
            for i in range(0, N - ran_num):
                j = i + ran_num
                min_height = 100000000000
                for k in range(i, j + 1):
                    if heights[k] < min_height:
                        min_height = heights[k]
                total_rec = min_height * (j - i + 1)
                mat[i][j] = max(mat[i][j - 1], mat[i + 1][j], total_rec)
        return mat[0][N - 1]


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    print(solution.largestRectangleArea(heights))
