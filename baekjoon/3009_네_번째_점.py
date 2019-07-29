import sys
sys.stdin = open('3009.txt', 'r')

Xs = []
Ys = []

for i in range(3):
    inputs = list(map(int, input().split()))
    Xs.append(inputs[0])
    Ys.append(inputs[1])

Xs.sort()
Ys.sort()

if Xs[0] == Xs[1]:
    X_answer = Xs[2]
else:
    X_answer = Xs[0]
    
if Ys[0] == Ys[1]:
    Y_answer = Ys[2]
else:
    Y_answer = Ys[0]

print(X_answer, Y_answer)