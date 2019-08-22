import sys
sys.stdin = open('10814.txt', 'r')

N = int(input())
members = [0] * N

for i in range(N):
    member = list(input().split())
    member[0] = int(member[0])
    members[i] = member

members.sort(key=lambda x: x[0])

for member in members:
    member[0] = str(member[0])
    print(' '.join(member))