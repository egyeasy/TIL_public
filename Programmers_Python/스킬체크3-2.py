g_tickets = []
length = 0
visited = []
results = []
best_result = []

def dfs(s, depth, result):
    global best_result
    print(visited)
    visited[s] = 1
    if depth == length:
        print("result", result)
        if not best_result:
            best_result = result
        else:
            is_best = False
            for i in range(length):
                if best_result[i] == result[i]:
                    continue
                elif best_result[i] < result[i]:
                    break
                else:
                    is_best = True
                    break
            if is_best:
                best_result = result
        results.append(result)
        return
    for i in range(length):
        print(i, g_tickets)
        if not visited[i] and g_tickets[s][1] == g_tickets[i][0]:
            dfs(i, depth + 1, result + [g_tickets[i][1]])

def solution(tickets):
    global g_tickets, length, visited, best_result
    g_tickets = tickets
    length = len(tickets)
    for idx in range(length):
        if g_tickets[idx][0] == "ICN":
            visited = [0] * length
            dfs(idx, 1, g_tickets[idx])
    print(results)
    print("best", best_result)
    return best_result

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])