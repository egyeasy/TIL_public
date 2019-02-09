n = int(input())
stars = [""] * 3
for i in range(1, 4):
    stars[i-1] = " "*(3-i)+"*"*(2*i-1)+" "*(3-i)
stars[1] = " * * "
for i in stars:
    print(i)

def upgrade(stars, n):
    stars = stars*3
    for i in range(n//2):
        stars[i] = " "*(n//2 - i) + stars[i]

upgrade(stars, n)

for i in stars:
    print(i)