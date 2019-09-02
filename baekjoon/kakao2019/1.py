# import sys
# sys.stdin = open('1.txt', 'r')

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
results = []
len_results = 0
users = {}
answer = []
for command in record:
    sp_comm = list(command.split())
    # print("sp_comm: ", sp_comm)
    if sp_comm[1] in users: # 개선사항 - 이걸 Enter에서만 실시할 것
        if sp_comm[0] == 'Enter':
            # 모두 바꿔주기
            # for result in results:
            #     print(result)
                # if result[1] == sp_comm[1]:
                #     result[2] = sp_comm[2]
            users[sp_comm[1]] = sp_comm[2]
            # 하나 추가
            results.append(sp_comm[:2])
        elif sp_comm[0] == 'Leave':
            # 하나 추가
            results.append(sp_comm[:2])
        else:
            # 유저 아이디 바꾸기
            users[sp_comm[1]] = sp_comm[2]
            # 모두 바꿔주기
            # for result in results:
            #     if result[1] == sp_comm[1]:
            #         result[2] = sp_comm[2]
    else:
        if sp_comm[0] == 'Enter':
            results.append(sp_comm[:2])
            users[sp_comm[1]] = sp_comm[2]
        else:
            print("에러")      

for result in results:
    if result[0] == 'Enter':
        answer.append("{}님이 들어왔습니다.".format(users[result[1]]))
    elif result[0] == 'Leave':
        answer.append("{}님이 나갔습니다.".format(users[result[1]]))

for i in answer:
    print(i)