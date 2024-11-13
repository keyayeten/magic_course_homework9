# Создайте класс Loan, который хранит сумму кредита.
# Реализуйте методы __add__ для увеличения суммы кредита
# (например, добавление начисленных процентов) и __sub__
# для его уменьшения (например, при выплате).
# Реализуйте также __mul__ для расчета увеличения суммы кредита
# при умножении на процентный коэффициент.

class Loan:
    def __init__(self, summa):
        self.summa = summa

    def __add__(self, other):
        return Loan(self.summa + other.summa)

    def __sub__(self, other):
        return Loan(self.summa - other.summa)

    def __mul__(self, other):
        procent = self.summa * other
        return Loan(procent)

    def __repr__(self):
        return f"Loan {self.summa}"


total_sum1 = Loan(20000)
total_sum2 = Loan(1000)
print(total_sum1 + total_sum2)
print(total_sum1 - total_sum2)
print((total_sum1 * 0.27) + total_sum1)

