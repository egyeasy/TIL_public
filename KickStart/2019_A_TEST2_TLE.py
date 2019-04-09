import sys
sys.stdin = open('2019_A.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N_people, num_team = map(int, input().split())
    players = list(map(int, input().split()))
    global_min_hours = 1000000000000
    # 오름차순으로 정렬
    players.sort(reverse=True)
    for start_idx in range(N_people - num_team + 1):
        # curr_team = players[start_idx: start_idx + num_team]
        # print(curr_team)
        # 정렬되어있으므로 최대치는 맨왼쪽
        max_rating = players[start_idx]
        total_needed_hours = num_team * max_rating - sum(players[start_idx: start_idx + num_team])
        # for i in range(start_idx, start_idx + num_team):
        #     total_needed_hours -= players[i]
        if total_needed_hours < global_min_hours:
            global_min_hours = total_needed_hours
            # 이 아래를 없애면 Runtime Error가 나는데 왜 그럴까?
            if global_min_hours == 0:
                break
    print("Case #{}: {}".format(tc, global_min_hours))
