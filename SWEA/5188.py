def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r - 1] = an[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)

comb(6, 3)

T = int(input())

for tc in range(1, T+1):
    m = int(input())
    an = []
    tr = []

    

