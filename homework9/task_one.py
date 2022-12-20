class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if self._check_if_exitst_triangel(side_a, side_b, side_c):
            self.a = side_a
            self.b = side_b
            self.c = side_c

    def _check_if_exitst_triangel(self, side_a, side_b, side_c,):
        if side_a + side_b > side_c:
            return True
        raise ValueError('sum of two sides must be greater than the third')

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        return False

    def perimetr(self):
        return self.a + self.b + self.c

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Sekond argument not Triangle')
        perimetr1 = self.perimetr()
        perimetr2 = other.perimetr()
        return perimetr1 == perimetr2


tr1 = Triangle(3, 4, 5)
print(tr1.is_right_angled())

try:
    tr2 = Triangle(10, 10, 22)
except ValueError as error_text:
    print(error_text)

tr3 = Triangle(11, 11, 20)
print(tr3.is_right_angled())

print(tr3 != tr1)
