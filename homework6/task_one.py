from math import sqrt


def distance(*args):
    point_x = 0
    point_y = 0
    result_distance = 0
    for element in args:
        point_x1 = element[0]
        point_y1 = element[1]
        if point_x == 0 and point_y == 0:
            point_x = point_x1
            point_y = point_y1
        else:
            dis = sqrt((point_x - point_x1)**2 + (point_y - point_y1)**2)
            print(f'Промежуточное расстояние между точками: {dis}')
            result_distance += dis
    print(f'Длинна маршрута между точками: {result_distance}')


a = (5, 6)
b = (3, 4)
c = (8, 9)
d = (10, 15)

distance(a, b, c, d)
