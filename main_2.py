import math

def triangle_area(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Стороны не могут образовать треугольник")

    s = (a + b + c) /2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print('Введите длины сторон треугольника a, b и c:')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    area = triangle_area(a, b, c)
    print(f"Площадь треугольника равна: {area}")

