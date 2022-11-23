from math import sqrt

point_by_x = input('Введите координату x: ')
point_by_y = input('Введите координату y: ')

point_by_x1 = input('Введите координату x1: ')
point_by_y1 = input('Введите координату y1: ')

point_by_x = float(point_by_x)
point_by_x1 = float(point_by_x1)
point_by_y = float(point_by_y)
point_by_y1 = float(point_by_y1)

distance = sqrt((point_by_x - point_by_x1)**2 + (point_by_y - point_by_y1)**2)

print(f'Расстояние между точками: {distance}')
