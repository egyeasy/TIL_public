class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] < 0:
                    count += N - j
                    break
        return count