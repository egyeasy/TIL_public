class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        top_maxes = []
        left_maxes = []
        
        total_add = 0
        
        for i in range(N):
            left_maxes.append(max(grid[i]))
            col_max = -1
            for j in range(N):
                if grid[j][i] > col_max:
                    col_max = grid[j][i]
            top_maxes.append(col_max)
        
        
        for i in range(N):
            for j in range(N):
                diff = min(left_maxes[i], top_maxes[j]) - grid[i][j]
                total_add += diff
                
        return total_add