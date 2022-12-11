import math


def distance(*args):
    distance = 0
    for index, coordinates in enumerate(args):
        if index == len(args)-1:
            break
        x, y = coordinates
        x1, y1 = args[index+1]
        function_formula = round(math.sqrt((x1 - x)**2 + (y1 - y)**2), 3)
        distance += function_formula
    return distance


result = distance((2, 2), (1, 1), (3, 2), (5, 7))
result = distance((1, 2), (1, 1), (3, 2))
print(result)
