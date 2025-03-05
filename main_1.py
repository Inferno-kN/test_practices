import math

def find_quad(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)

        return root

    else:
        return "У уравнения нет действительных корней"

def main():
    print('Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0')
    a = float(input("Введите а >>"))
    b = float(input("Введите b >>"))
    c = float(input("Введите с >> "))

    roots = find_quad(a, b, c)

    if roots == 2:
        print(f"У уравнения два корня: {roots[0], "и" + roots[1]}")

    elif roots is None:
        print("Уравнения не имеет корней, тк дискриминант отрицательный")

    else:
        print(f"У уравнения только один корень: {roots[0]}")