import sys
sys.stdin = open('1181.txt', 'r')

N = int(input())
num_dict = {}
for i in range(1, 51):
    num_dict[i] = []
for _ in range(N):
    word = input()
    leng = len(word)
    num_dict[leng].append(word)

for key, item in num_dict.items():
    item.sort()
    prev_word = ''
    for word in item:
        if word != prev_word:
            print(word)
            prev_word = word
    
