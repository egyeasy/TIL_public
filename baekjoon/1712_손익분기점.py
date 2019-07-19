import sys
sys.stdin = open('1712.txt', 'r')

fixed_cost, variable_cost, price = map(int, input().split())

if variable_cost >= price:
    print(-1)
else:
    sales = int(fixed_cost/(price - variable_cost)) + 1
    print(sales)
