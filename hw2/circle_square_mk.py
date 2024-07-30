import random
import math

def circle_square_mk(r,n):
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < r**2:
            count += 1
    return 4 * (count / n)
