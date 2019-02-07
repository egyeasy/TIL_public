alist = list(range(1, 10001))
for i in range(1, 10001):
    if i + sum(map(int, str(i))) in alist:
        alist.remove(i + sum(map(int, str(i))))
for i in alist:
    print(i)