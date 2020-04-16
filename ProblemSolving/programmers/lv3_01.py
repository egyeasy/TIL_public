from collections import deque

def bfs(s, mat, N, K):
    visited = [0] * (N+1)
    dq = deque()
    dq.append(s)
    
    while dq:
        s = dq.popleft()
        for i in range(2, N + 1):
            leng = mat[s][i]
            if leng and visited[s] + leng <= K and (not visited[i] or visited[s] + leng < visited[i]):
                visited[i] = visited[s] + leng
                dq.append(i)
    return visited

def solution(N, road, K):
    answer = 0
    mat = [[0] * (N+1) for _ in range(N+1)]
    
    for arr in road:
        start = arr[0]
        end = arr[1]
        length = arr[2]
        if not mat[start][end] or length < mat[start][end]:
            mat[start][end] = length
            mat[end][start] = length

    # for i in mat:
    #     print(i)
        
    visited = bfs(1, mat, N, K)
    
    for i in visited:
        if i:
            answer += 1
    
    # print(visited)

    return answer + 1