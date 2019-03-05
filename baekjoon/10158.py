import sys
sys.stdin = open('10158.txt', 'r')

def isWall():
    if (s_row == 0 or s_row == m_row) and (s_col == 0 or s_col == m_col):
        return "corner"
    elif s_row == 0 or s_row == m_row or s_col == 0 or s_col == m_col:
        return "wall"

def change(dir, word):
    if word == "corner":
        if dir == 0 or dir == 2:
            return dir + 1
        else:
            return dir - 1
    elif word == "wall":
        if dir == 0:
            if s_col == m_col:
                return 3
            elif s_row == m_row:
                return 2
        elif dir == 1:
            if s_col == 0:
                return 2
            elif s_row == 0:
                return 3
        elif dir == 2:
            if s_col == m_col:
                return 1
            elif s_row == 0:
                return 0
        else:
            if s_col == 0:
                return 0
            elif s_row == m_row:
                return 1

m_row, m_col = map(int, input().split())
s_row, s_col = map(int, input().split())
max_t = int(input())
curr_t = 0
dx = [1, -1, -1, 1]
dy = [1, -1, 1, -1]
dir = 0
while curr_t != max_t:
    iswall = isWall()
    if iswall == "corner":
        dir = change(dir, "corner")
    elif iswall == "wall":
        dir = change(dir, "wall")
    s_row += dx[dir]
    s_col += dy[dir]
    curr_t += 1

print(s_row, s_col)
