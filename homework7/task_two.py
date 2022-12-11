def is_right_angle_triangle(a, b, c):
    sort_list = sorted([a, b, c])
    c = float(sort_list[2])
    a = float(sort_list[0])
    b = float(sort_list[1])
    if a + b > c and a + c > b and b + c > a:
        if c**2 == a**2 + b**2:
            print('description: the triangle is right-angled')
            return True
        else:
            print('description: the triangle is not right-angled')
            return True
    else:
        print('description: no such triangle exists')
        return False


result = is_right_angle_triangle(3, 5, 4)
# result = is_right_angle_triangle(3, 5, 9)
# result = is_right_angle_triangle(11, 11, 21)
print(result)
