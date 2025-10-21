class Triangle:
    def __init__(self, a, b, c):
        if is_valid_triangle(a,b,c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('Triangle with such sides cannot exist')

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        half_p = self.get_perimeter() / 2.0
        area = (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5
        return area

def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)
