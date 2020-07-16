from typing import List

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]

def go(i, j, dir):
    i += d_row[dir]
    j += d_col[dir]
    return i, j

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        M = len(grid)
        N = len(grid[0])
        i, j = 0, 0
        dir = 0
        while 0 <= i < M and 0 <= j < N:
            print(i, j)
            if grid[i][j] < 0:
                if dir == 0:
                    count += N - j
                    print("count: ", count)
                    dir = 1
                elif dir == 1:
                    dir = 2
                elif dir == 2 and j == 0:
                    count += N
                    i += 1
                    j += 1
            else:
                if dir == 2:
                    count += N - j - 1
                    print("count: ", count)
                    dir = 1
                elif dir == 0 and j == N - 1:
                    dir = 1
                elif dir == 1:
                    if j != N - 1:
                        dir = 0
            i, j = go(i, j, dir)
        print(count)
        return count

if __name__ == "__main__":
    grid = [[3,2],[1,0]]
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    #grid = [[-1]]
    #grid = [[0]]
    #grid = [[1,-1],[-1,-1]]
    #grid = [[6,5],[5,0],[4,-1]]
    #grid = [[3,2],[-3,-3],[-3,-3],[-3,-3]]
    sol = Solution()
    sol.countNegatives(grid)

