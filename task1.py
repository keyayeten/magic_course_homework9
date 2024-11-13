# Класс для работы с векторами на плоскости.
# Создайте класс Vector2D для двумерных векторов
# с методами сложения, вычитания и умножения на скаляр.
# Реализуйте магические методы __add__, __sub__ и __mul__,
# чтобы перегрузить операторы +, -, и *.

# Vector2D(1, 2) + Vector2D(2, 3) = Vector2D(3, 5)
# Vector2D(2, 3) * 3 = Vector2D(6, 9)

class Vector2D:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        t1 = self.a + other.a
        t2 = self.b + other.b
        return Vector2D(t1, t2)

    def __sub__(self, other):
        t1 = self.a - other.a
        t2 = self.b - other.b
        return Vector2D(t1, t2)

    def __mul__(self, other=3):
        t1 = self.a * other
        t2 = self.b * other
        return Vector2D(t1, t2)



    def __repr__(self):
        return f"Vector2D {self.a}, {self.b}"

a = Vector2D(1, 2)
a2 = Vector2D(2, 3)
print(a + a2)
print(a - a2)
print(a * 3)
print(a2 * 3)
