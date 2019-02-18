import math

def polysum(n, s):
    numerator = 0.25 * n * (s**2)
    denominator = math.tan(math.pi/n)
    area = numerator/denominator
    perimeter = n * s
    return round(area + perimeter**2, 4)