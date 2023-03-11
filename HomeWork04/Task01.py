# Вычислить число pi c заданной точностью d
# Пример:
# - при d = 3, π = 3.141
#
# формула: pi = sum(n=0, n=inf)( (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6)) )
from decimal import Decimal
from decimal import getcontext
# import decimal

PI = Decimal(3.14159265358979323846264338327950288419716939937510_5820974944_5923078164_0628620899_8628034825_3421170679)

getcontext().prec = 100

# d = int(input('Введите точность: '))
d = 50  # int(input('Введите точность: '))
calc_pi = Decimal(0)
check = Decimal(0)

for n in range(int(10000)):
    calc_pi += Decimal(Decimal(1 / 16 ** n)) * \
               Decimal((4 / Decimal(8 * n + 1)) -
                       Decimal(2 / Decimal(8 * n + 4)) -
                       Decimal(1 / Decimal(8 * n + 5)) -
                       Decimal(1 / Decimal(8 * n + 6)))
    if abs(check - calc_pi) < 10 ** (-d):
        break
    check = calc_pi

# print('pi = ', round(calc_pi, d))
print('pi = ', calc_pi)
print(type(calc_pi), type(PI), calc_pi - PI)

