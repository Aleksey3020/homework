import math
coordinate1 = float(input('Введите координату x: '))
coordinate2 = float(input('Введите координату y: '))
coordinate3 = float(input('Введите координату x1: '))
coordinate4 = float(input('Введите координату y1: '))

distance = round(math.sqrt((coordinate3 - coordinate1)**2 +
                 (coordinate4 - coordinate2)**2), 2)

print(f"Растояние между точками: {distance}")
