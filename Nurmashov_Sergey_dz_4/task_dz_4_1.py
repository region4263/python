# Вычислить число π c заданной точностью d

from math import pi

d = 1
while 10 ** (-10) >= d or d >= 0.1:
    d = float(input('введите заданную точность (от 0.1 до 10 в степени -10): '))
total = round(pi, len(str(d)) - 2)
print(total)
