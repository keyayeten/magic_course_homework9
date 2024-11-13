# Создайте класс Angle, который хранит значение угла в градусах.
# Реализуйте __add__ и __sub__, чтобы складывать и вычитать углы.

# Angle(130) + Angle(50) = Angle(0)
# Angle(50) - Angle(130) = Angle(80)

class Angle():
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if (self.a + other.a) == 180:
            return Angle(0)
        return Angle(self.a + other.a)


    def __sub__(self, other):
        yg = (self.a - other.a)
        return Angle(abs(yg))


    def __repr__(self):
        return f"Angle({self.a})"

ygol = Angle(130)
ygol2 = Angle(50)
ygol3 = Angle(10)
print(ygol + ygol2)
print(ygol2 - ygol)
print(ygol2 + ygol3)