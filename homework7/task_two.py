def is_right_angle_triangle(a, b, c):
    sort_list = sorted([a, b, c])
    c = float(sort_list[2])
    a = float(sort_list[0])
    b = float(sort_list[1])
    to_print = {}
    if a + b > c and a + c > b and b + c > a:
        if c**2 == a**2 + b**2:
            to_print['description'] = 'the triangle is right-angled'
            to_print['result'] = 'True'
            print(to_print)
        else:
            to_print['description'] = 'the triangle is not right-angled'
            to_print['result'] = 'True'
            print(to_print)
    else:
        to_print['description'] = 'no such triangle exists'
        to_print['result'] = 'False'
        print(to_print)


result = is_right_angle_triangle(3, 5, 4)
# result = is_right_angle_triangle(3, 5, 9)
# result = is_right_angle_triangle(11, 11, 21)
