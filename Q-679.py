def slope(x1, y1, x2, y2):
    if x1 == x2:
        print("Slope: Undefined")
        return "Undefined"
    result = (y2 - y1) / (x2 - x1)
    print(f"Slope: {result}")
    return result

slope(1, 2, 3, 4)
slope(1, 2, 1, 5)
