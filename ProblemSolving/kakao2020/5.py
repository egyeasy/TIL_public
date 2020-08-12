# 통과 못함

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

grid = [[0]*(n + 1) for _ in range(n + 1)]

def build(x, y, is_bo):
    grid[x][y] = [x, y, is_bo]

def delete(x, y, is_bo):
    grid[x][y] = 0

def bo_right_ok(x, y):
    if x+1<=n and grid[x+1][y] and grid[x+1][y][2]:
        # 보와 연결 or 다리 있으면
        if (x+2<=n and grid[x+2][y] and grid[x+2][y][2]) or (x+2<=n and y-1>=0 and grid[x+2][y-1] and not grid[x+2][y-1][2]):
            return True
    return False

def bo_left_ok(x, y):
    if x-1>=0 and grid[x-1][y] and grid[x-1][y][2]:
        #보와 연결 or 다리 있으면
        if (x-2>=0 and grid[x-2][y] and grid[x-2][y][2]) or (x-2>=0 and y-1>=0 and grid[x-2][y-1] and not grid[x-2][y-1][2]):
            return True
    return False

def solution(n, build_frame):
    for comm in build_frame:
        print(comm)
    # 보인지
    x, y, is_bo, is_build = comm
    if is_bo:
        # 설치인지
        if is_build:
            # 한칸 아래 기둥이나 
            if (0<=y-1 and grid[x][y-1] and not grid[x][y-1][2]) or (0<=y-1 and grid[x + 1][y-1] and not grid[x+1][y-1][2]) or (0<=x-1 and grid[x-1][y] and grid[x-1][y][2]) or (x+1<=n and grid[x+1][y] and grid[x+1][y][2]):
                build(x, y, is_bo)
        # 삭제인지
        else:
            # 기둥과 연결
            if (grid[x][y-1] and not grid[x][y-1][2]) and (grid[x+1][y-1] and not grid[x+1][y-1][2]):
                delete(x, y, is_bo)
            # 한쪽 기둥과 연결
            elif (grid[x][y-1] and not grid[x][y-1][2]):
                # 보와 연결
                if x+1<=n and grid[x+1][y] and grid[x+1][y][2]:
                    # 보와 연결 or 다리 있으면 삭제
                    if (x+2<=n and grid[x+2][y] and grid[x+2][y][2]) or (x+2<=n and y-1>=0 and grid[x+2][y-1] and not grid[x+2][y-1][2]):
                        delete(x, y, is_bo)
                # 아무것도 안 연결
                elif x+1<=n and not grid[x+1][y]:
                    delete(x, y, is_bo)
            elif (grid[x+1][y-1] and not grid[x+1][y-1][2]):
                # 보와 연결
                if x-1>=0 and grid[x-1][y] and grid[x-1][y][2]:
                    #보와 연결 or 다리 있으면 삭제
                    if (x-2>=0 and grid[x-2][y] and grid[x-2][y][2]) or (x-2>=0 and y-1>=0 and grid[x-2][y-1] and not grid[x-2][y-1][2]):
                        delete(x, y, is_bo)
                # 아무것도 안 연결
                elif x-1>=0 and not grid[x-1][y]:
                    delete(x, y, is_bo)
            # 양쪽 보와 연결
            elif (x-1>=0 and x+1<=n and grid[x-1][y] and grid[x-1][y][2] and grid[x+1][y] and grid[x+1][y][2]):
                # 우측 보 확인
                if x+1<=n and grid[x+1][y] and grid[x+1][y][2]:
                    # 보와 연결 or 다리 있으면 삭제
                    if (x+2<=n and grid[x+2][y] and grid[x+2][y][2]) or (x+2<=n and y-1>=0 and grid[x+2][y-1] and not grid[x+2][y-1][2]):
                        # 좌측 보 확인
                        if x-1>=0 and grid[x-1][y] and grid[x-1][y][2]:
                            #보와 연결 or 다리 있으면 삭제
                            if (x-2>=0 and grid[x-2][y] and grid[x-2][y][2]) or (x-2>=0 and y-1>=0 and grid[x-2][y-1] and not grid[x-2][y-1][2]):
                                delete(x, y, is_bo)
    # 기둥인지
    else:
        # 설치인지
        if is_build:
            if y == 0 or (0<=y-1 and grid[x][y - 1]):
                build(x, y, is_bo)
        # 삭제인지
        else:
            # 위가 기둥
            if y+1<=n and grid[x][y + 1] and not grid[x][y + 1][2]:
                pass
            # 양쪽 보
            elif grid[x-1][y+1] and grid[x-1][y+1][2] and grid[x][y+1] and grid[x][y+1][2]:
                if bo_left_ok(x-1, y+1) and bo_right_ok(x, y+1):
                    delete(x, y, is_bo)
            # 왼쪽이 보
            elif grid[x-1][y+1] and grid[x-1][y+1][2] and bo_left_ok(x-1, y+1):
                delete(x, y, is_bo)
            # 오른쪽이 보
            elif grid[x][y+1] and grid[x][y+1][2] and bo_right_ok(x, y+1):
                delete(x, y, is_bo)
            # 아무것도 없음
            elif grid:
                delete(x, y, is_bo)

    
    answer = [[]]
    print()
    print(answer)
    return answer

solution(n, build_frame)