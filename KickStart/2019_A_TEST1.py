import sys
sys.stdin = open('2019_A.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N_people, num_team = map(int, input().split())
    players = list(map(int, input().split()))
    global_min_hours = 1000000000000
    players.sort(reverse=True)
    for start_idx in range(N_people - num_team + 1):
        curr_team = players[start_idx: start_idx + num_team]
        # print(curr_team)
        max_rating = max(curr_team)
        total_needed_hours = 0
        for player in curr_team:
            total_needed_hours += max_rating - player
        if total_needed_hours < global_min_hours:
            global_min_hours = total_needed_hours
            if global_min_hours == 0:
                break
    print("Case #{}: {}".format(tc, global_min_hours))
