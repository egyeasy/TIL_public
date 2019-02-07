n = int(input())
stars = [""] * n
for i in range(1, n+1):
    stars[i-1] = " "*(n-i)+"*"*(2*i-1)

for i in stars:
    print(i)