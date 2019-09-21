board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

from collections import deque

dq = deque()

def bfs(pos, total_len, board):
    dq.append(pos)
    while dq:
        s = dq.popleft()
        posit1, posit2, dir, former, time = s
        if posit2 == [total_len - 1, total_len - 1]:
            return time
        # print(posit1, posit2)
        if dir == 'garo':
            # 가로이동
            if posit2[1] + 1 < total_len and board[posit2[0]][posit2[1]+1] == 0:
                # print("garo-garo")
                posit1[1] += 1
                posit2[1] += 1
                new1 = posit1[:]
                new2 = posit2[:]
                dq.append([new1, new2, dir, 0, time + 1])
                posit1[1] -= 1
                posit2[1] -= 1
            # 세로이동
            if posit1[0] + 1 < total_len and board[posit1[0]+1][posit1[1]] == 0 and board[posit2[0]+1][posit2[1]] == 0:
                # print("garo-sero")
                posit1[0] += 1
                posit2[0] += 1
                new1 = posit1[:]
                new2 = posit2[:]
                dq.append([new1, new2, dir, 0, time + 1])
                posit1[0] -= 1
                posit2[0] -= 1
            # 대각 1
            if posit1[0] + 1 < total_len and board[posit1[0]+1][posit1[1]] == 0 and board[posit2[0]+1][posit2[1]] == 0:
                # print("garo-dig1")
                posit1[1] += 1
                posit2[0] += 1
                new1 = posit1[:]
                new2 = posit2[:]
                dq.append([new1, new2, 'sero', 'garodig1', time + 1])
                # 대각 2
                if former != 'serodig1':
                    # print("garo-dig2")
                    posit1[1] -= 1
                    posit2[1] -= 1
                    new1 = posit1[:]
                    new2 = posit2[:]
                    dq.append([new1, new2, 'sero', 'garodig2', time + 1])
                    posit2[0] -= 1
                    posit2[1] += 1
        else:
            # 가로 이동
            if posit1[1] + 1 < total_len and board[posit1[0]][posit1[1]+1] == 0 and board[posit2[0]][posit2[1]+1] == 0:
                # print("sero-garo")
                posit1[1] += 1
                posit2[1] += 1
                new1 = posit1[:]
                new2 = posit2[:]
                dq.append([new1, new2, dir, 0, time + 1])
                posit1[1] -= 1
                posit2[1] -= 1
            # 세로 이동
            # print(posit1, posit2)
            if posit2[0] + 1 < total_len and board[posit2[0] + 1][posit2[1]] == 0:
                # print("sero-sero")
                posit1[0] += 1
                posit2[0] += 1
                new1 = posit1[:]
                new2 = posit2[:]
                dq.append([new1, new2, dir, 0, time + 1])
                posit1[0] -= 1
                posit2[0] -= 1
            # 대각 1
            if posit1[1] + 1 < total_len and board[posit1[0]][posit1[1]+1] == 0 and board[posit2[0]][posit2[1]+1] == 0:
                if former != 'garodig2':
                    # print("sero-dig1")
                    posit2[0] -= 1
                    posit2[1] += 1
                    new1 = posit1[:]
                    new2 = posit2[:]
                    dq.append([new1, new2, 'garo', 'serodig1', time + 1])
                    posit1[0] += 1
                    posit2[0] += 1
                    # 대각 2
                    # print("sero-dig2")
                    new1 = posit1[:]
                    new2 = posit2[:]
                    dq.append([new1, new2, 'garo', 'serodig2', time + 1])
                    posit1[0] -= 1
                    posit2[1] -= 1
                else:
                    # print("sero-dig2")
                    new1 = posit1[:]
                    new2 = posit2[:]
                    dq.append([new1, new2, 'garo', 'serodig2', time + 1])
                    posit1[0] += 1
                    posit2[1] += 1

        
    


def solution(board):
    answer = 0
    total_len = len(board)
    # for i in board:
    #     print(i)
    # print()
    pos = [[0, 0], [0, 1], 'garo', 0, 0]
    answer = bfs(pos, total_len, board)
    # print(answer)
    return answer


solution(board)
