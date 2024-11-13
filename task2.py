# # Создайте класс FileSize, который хранит размер файла в байтах.
# Реализуйте методы __add__, __sub__ и __mul__,
# чтобы можно было складывать размеры файлов,
# вычитать их и умножать на целое число для вычисления объема
# нескольких файлов одинакового размера.

class FileSize:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        if other.size < 0 or self.size < 0:
            return 'Не верный размер'
        return FileSize(self.size + other.size)

    def __sub__(self, other):
        if other.size < 0 or self.size < 0:
            return 'Не верный размер'
        r = (self.size - other.size)
        if r < 0:
            return 'Недостаточно места'
        return FileSize(r)

    def __mul__(self, other):
        if other < 0 or self.size < 0:
            return 'Не верный размер'
        return FileSize(self.size * other)
    def __repr__(self):
        return f'{self.size}'

size1 = FileSize(5)
size2 = FileSize(10)
print(size1 + size2)
print(size1 - size2)
print(size1 * -2)
print(size2 * 8)
