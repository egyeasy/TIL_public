total_count = 0
visited = []

def make_visited_from(row: int, col: int, n: int) -> None:
    visited[row][col] = 1
    left_row = row + 1
    left_col = col - 1
    right_row = row + 1
    right_col = col + 1
    down_row = row + 1
    while left_row < n and 0 <= left_col < n:
        visited[left_row][left_col] += 1
        left_row += 1
        left_col -= 1
    while right_row < n and 0 <= right_col < n:
        visited[right_row][right_col] += 1
        right_row += 1
        right_col += 1
    while down_row < n:
        visited[down_row][col] += 1
        down_row += 1
        
def undo_visited_from(row: int, col: int, n: int) -> None:
    visited[row][col] = 0

    left_row = row + 1
    left_col = col - 1
    right_row = row + 1
    right_col = col + 1
    down_row = row + 1
    while left_row < n and 0 <= left_col < n:
        visited[left_row][left_col] -= 1
        left_row += 1
        left_col -= 1
    while right_row < n and 0 <= right_col < n:
        visited[right_row][right_col] -= 1
        right_row += 1
        right_col += 1
    while down_row < n:
        visited[down_row][col] -= 1
        down_row += 1

def backtrack(total_level: int, level: int) -> None:
    global total_count
    if level == total_level:
        total_count += 1
        return
    for i in range(total_level):
        if not visited[level][i]:
            make_visited_from(level, i, total_level)
            backtrack(total_level, level + 1)
            undo_visited_from(level, i, total_level)

class Solution:
    def totalNQueens(self, n: int) -> int:
        global total_count, visited
        total_count = 0
        visited = [[0] * n for _ in range(n)]
        backtrack(n, 0)
            
        return total_count

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(4))