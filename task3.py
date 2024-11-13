# Создайте класс Angle, который хранит значение угла в градусах.
# Реализуйте __add__ и __sub__, чтобы складывать и вычитать углы.

# Angle(130) + Angle(50) = Angle(0)
# Angle(50) - Angle(130) = Angle(80)

class Angle():
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Angle(self.a + other.a)


    def __sub__(self, other):
        return Angle(self.a - other.a)

    def __repr__(self):
        return f"Angle({self.a})"

ygol = Angle(130)
ygol2 = Angle(50)
print(ygol + ygol2)
print(ygol - ygol2)