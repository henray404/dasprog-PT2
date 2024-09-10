def quadrant_location(x1, y1):

    if x1 > 0 and y1 > 0:
        return "kuadrant 1"
    if x1 < 0 and y1 > 0:
        return "kuadrant 2"
    if x1 < 0 and y1 < 0:
        return "kuadrant 3"
    if x1 > 0 and y1 < 0:
        return "kuadrant 4"
    if x1 == 0 and y1 == 0:
        return "origin point"
    if x1 == 0:
        return "y-axis"
    if y1 == 0:
        return "x-axis"


x1, y1 = input("input first x and y:").split(" ")
x1 = float(x1)
y1 = float(y1)
print(f"({x1}, {y1}) is in " + quadrant_location(x1, y1))
