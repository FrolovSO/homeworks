class Triangle:
    def __init__(self, a, b, c):
        try:
            if self._check_triangle_exist(a, b, c):
                self.a = a
                self.b = b
                self.c = c
        except ValueError as e:
            print(e)

    def _check_triangle_exist(self, a, b, c):
        if (a + b > c and a + c > b and b + c > a):
            return True
        raise ValueError('No such triangle exists')

    def is_right_angled(self):
        try:
            if self.c**2 == self.a**2 + self.b**2:
                return True
            else:
                return False
        except AttributeError as e:
            print(e)

    def perimetr(self):
        return self.a + self.b + self.c

    def __eq__(self, other):
        perimetr1 = self.perimetr()
        perimetr2 = other.perimetr()
        return perimetr1 == perimetr2


t1 = Triangle(3, 4, 5)
t2 = Triangle(10, 10, 22)
t3 = Triangle(11, 11, 20)
print(t1.is_right_angled())
print(t3.is_right_angled())
print(t1 != t3)
