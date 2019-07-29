import sys
sys.stdin = open('3053.txt', 'r')

import math

R = float(input())

print(R**2 * math.pi)
print((R * 2**(1/2))**2)