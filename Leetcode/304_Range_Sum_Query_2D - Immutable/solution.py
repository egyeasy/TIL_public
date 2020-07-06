from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row_M = len(matrix)
        self.col_N = len(matrix[0]) if matrix else 0
        self.tree = [[0] * (self.col_N * 4) for _ in range(self.row_M)]
        for i in range(self.row_M):
            self.init_tree(i)

    def init_tree(self, row: int) -> None:
        for key, value in enumerate(self.matrix[row]):
            self.update(row, 1, 0, self.col_N - 1, key, value)

    def update(self, row: int, node: int, start: int, end: int, index: int, diff: int) -> None:
        if index < start or end < index:
            return
        self.tree[row][node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        self.update(row, node * 2, start, mid, index, diff)
        self.update(row, node * 2 + 1, mid + 1, end, index, diff)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1, row2 + 1):
            sum_ += self.sum_row(i, 1, 0, self.col_N - 1, col1, col2)
        
        return sum_
    
    def sum_row(self, row: int, node: int, start: int, end: int, range_left: int, range_right: int) -> int:
        if range_right < start or end < range_left:
            return 0
        if range_left <= start and end <= range_right:
            return self.tree[row][node]
        mid = (start + end) // 2
        return self.sum_row(row, node * 2, start, mid, range_left, range_right) +\
               self.sum_row(row, node * 2 + 1, mid + 1, end, range_left, range_right)

if __name__ == '__main__':
    matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]
    sol = NumMatrix(matrix)
    print(sol.sumRegion(2, 1, 4, 3))
    print(sol.sumRegion(1, 1, 2, 2))
    print(sol.sumRegion(1, 2, 2, 4))