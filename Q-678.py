import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Distance: {dist}")
    return dist

distance(0, 0, 3, 4)
