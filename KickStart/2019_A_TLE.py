import sys
sys.stdin = open('2019_A.txt', 'r')

from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N_people, num_team = map(int, input().split())
    players = list(map(int, input().split()))
    global_min_hours = 1000000000000
    for comb in combinations(players, num_team):
        max_rating = max(comb)
        total_needed_hours = 0
        for player_rating in comb:
            total_needed_hours += max_rating - player_rating
        if total_needed_hours < global_min_hours:
            global_min_hours = total_needed_hours
            if global_min_hours == 0:
                break

    print("Case #{}: {}".format(tc, global_min_hours))