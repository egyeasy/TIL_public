# 200702 다시 풀어보기
from collections import deque

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]
min_cost = 100000000000000


def bfs(s, len_N, board):
    global min_cost
    dq = deque()
    dq.append(s)
    visited = [[0] * len_N for _ in range(len_N)]
    while dq:
        s_row, s_col, curr_dir, curr_cost = dq.popleft()
        visited[s_row][s_col] = curr_cost
        if s_row == len_N - 1 and s_col == len_N - 1 and curr_cost < min_cost:
            min_cost = curr_cost
        for i in range(4):
            c_row = s_row + d_row[i]
            c_col = s_col + d_col[i]
            if (s_row, s_col) == (1, 2) and (c_row, c_col) == (2, 2):
                pass
            if (
                0 <= c_row < len_N
                and 0 <= c_col < len_N
                and not board[c_row][c_col]
                and (not visited[c_row][c_col] or curr_cost < visited[c_row][c_col])
            ):
                if curr_cost < min_cost:
                    if curr_dir == i:
                        dq.append((c_row, c_col, i, curr_cost + 100))
                    else:
                        dq.append((c_row, c_col, i, curr_cost + 600))


def solution(board):
    global min_cost
    len_N = len(board)

    bfs((0, 1, 0, 100), len_N, board)
    bfs((1, 0, 1, 100), len_N, board)

    return min_cost


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
# print(solution([[0, 0, 1, 0],
#                 [0, 0, 0, 0],
#                 [0, 1, 0, 1],
#                 [1, 0, 0, 0]]))
# print(
#     solution(
#         [
#             [0, 0, 0, 0, 0, 0],
#             [0, 1, 1, 1, 1, 0],
#             [0, 0, 1, 0, 0, 0],
#             [1, 0, 0, 1, 0, 1],
#             [0, 1, 0, 0, 0, 1],
#             [0, 0, 0, 0, 0, 0],
#         ]
#     )
# )
