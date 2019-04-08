import sys
sys.stdin = open('2019_A.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N_people, num_team = map(int, input().split())
    players = list(map(int, input().split()))
    team_list = [[] for _ in range(N_people)]
    # 각 player가 max인 team을 구성
    for player in players:
        team_list[0].append(player)


    global_min_hours = 1000000000000


    print("Case #{}: {}".format(tc, global_min_hours))
