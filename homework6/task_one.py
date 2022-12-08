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
            point_x = point_x1
            point_y = point_y1
    print(f'Длинна маршрута между точками: {result_distance}')


a = (1, 1)
b = (1, 2)
c = (2, 2)

distance(a, b, c)
