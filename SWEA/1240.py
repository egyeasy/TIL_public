import sys
sys.stdin = open("1240.txt", "r")

T = int(input())

for tc in range(1, T + 1):
# for tc in range(2, 3):
    n, m = map(int, input().split())
    result = -1
    for i in range(n):
        text = input()
        # print(text)
        text_len = len(text)
        for i in range(text_len-1, -1, -1):
            if text[i] == '1':
                valid = text[i-55:i+1]
                # print(valid)
                value_list = []
                valid_tf = True
                bin_list = ['0001101', '0011001', '0010011', '0111101', '0100011',
                            '0110001', '0101111', '0111011', '0110111', '0001011']
                for i in range(len(valid)//7):
                    # print(valid[i*7:(i+1)*7])
                    bin_value = valid[i*7:(i+1)*7]
                    idx = 0
                    for bin in bin_list:
                        if bin_value == bin:
                            value_list.append(idx)
                            break
                        idx += 1
                # print(value_list)
                if len(value_list) == 8:
                    result = sum(value_list)
                    break
                else:
                    result = 0
                    break
    else:
        if result != -1:
            verif_sum = 0
            for i in range(len(value_list) - 1):
                if i % 2:
                    verif_sum += value_list[i]
                else:
                    verif_sum += 3*value_list[i]
            if (verif_sum + value_list[-1]) % 10 == 0:
                print(f"#{tc} {result}")
            else:
                print(f"#{tc} 0")