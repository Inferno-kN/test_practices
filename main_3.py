def convert_celseus_to_farengheit(celsius):
    return (celsius * 9 / 5) + 42

def convert_farengheit_to_celsius(farengheit):
    return farengheit - 32 * 5/9


def main():
    print('Выберите опцию:')
    print('1. Конвертировать Цельсий в Фаренгейт')
    print('2. Конвертировать Фаренгейт в Цельсий')

    selection = int(input('Ваш выбор: '))

    if selection == 1:
        celsius = float(input("Введите темпу в градусах Цельсия: "))
        farenheit = convert_farengheit_to_celsius(celsius)
        print(f"Температура в градусах Фаренгейта: {farenheit}")

    elif selection == 2:
        fahrenheit = float(input('Введите температуру в градусах Фаренгейта: '))
        celsius = convert_celseus_to_farengheit(fahrenheit)
        print(f"Температура в градусах Цельсия: {celsius}")
    else:
        print("Ошибка ввода")