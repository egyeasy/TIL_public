import sys
f = open('lol.txt', 'r', encoding="utf8", newline="\n")

rank = []
while True:
    line = f.readline()
    if not line: break
    if line:
        word = line.split()[0]
        if word[-1] != "%":
            rank.append(word)
    
print(rank)

string = "아트록스, 아리, 아칼리, 아무무, 애니, 애쉬, 브랜드, 브라움, 케이틀린, 초가스, 다리우스, 드레이븐, 에코, 이즈리얼, 피오라, 피즈, 가렌, 그레이브즈, 이렐리아, 잔나, 자르반 4세, 잭스, 진, 징크스, 카르마, 카서스, 카타리나, 케일, 카직스, 르블랑, 리 신, 레오나, 루시안, 룰루, 럭스, 말파이트, 마오카이, 마스터 이, 미스 포츈, 모데카이저, 모르가나, 노틸러스, 니달리, 판테온, 파이크, 퀸, 레넥톤, 리븐, 라이즈, 시비르, 소나, 소라카, 쓰레쉬, 트리스타나, 트린다미어, 트위스티드 페이트, 트위치, 바루스, 베인, 베이가, 벨코즈, 블라디미르, 오공, 자야, 제드"
arr = string.split(", ")
arr.sort()
for item in arr:
    print(item, end=" ")



