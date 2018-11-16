import math
def calc(x):
    run1 = True
    def plus(xz, xzz):
        return xz + xzz
    def minus(xz, xzz):
        return xz - xzz
    def delen(xz, xzz):
        loop = True
        while loop:
            try:
                xzz = float(xzz)
                sa = 1 / xzz
                return xz / xzz
            except(TypeError,ValueError, ZeroDivisionError):
                print("Неккоректный ввод!")
                xzz = input("Введите второе число: ")
    def umn(xz, xzz):
        return xz * xzz
    def step(xz):
        return xz ** 2
    def kor(xz):
        loop = True
        while loop:
            try:
                loop = False
                return math.sqrt(xz)
            except ValueError:
                print("Некорректный ввод!")
                xz = input("Введите число: ")
                xz = search(xz)
    def sinus(xz):
        return math.sin(xz)
    def cosinus(xz):
        return math.cos(xz)
    def tang(xz):
        return math.tan(xz)
    def search(z):
        tt = True
        if tt == z.isdigit():
            nonlocal run1
            run1 = False
            return z
    def score(s):
        nonlocal run1
        if "1" <= x <= "4":
            while run1:
                a = input("Введите первое число: ")
                a = search(a)
            a = float(a)
            run1 = True
            while run1:
                b = input("Введите второе число: ")
                b = search(b)
            b = float(b)
            if s == "1":
                print("Ответ:", plus(a, b))
            elif s == "2":
                print("Ответ:", minus(a, b))
            elif s == "3":
                print("Ответ:", delen(a, b))
            elif s == "4":
                print("Ответ:", umn(a, b))
        elif "5" <= s <= "9":
            while run1:
                a = input("Введите число: ")
                a = search(a)
            a = float(a)
            if s == "5":
                print("Ответ:", step(a))
            elif s == "6":
                print("Ответ:", kor(a))
            elif s == "7":
                print("Ответ:", sinus(a))
            elif s == "8":
                print("Ответ:", cosinus(a))
            elif s == "9":
                print("Ответ:", tang(a))
    score(x)
run = True
run2 = True
while run2:
    print("Хотите начать?")
    print("1.Да     2.Нет")
    start = input()
    if start == "1":
        while run:
            print("""
    1.Сложение
    2.Вычитание
    3.Деление
    4.Умножение
    5.Возведение в степень
    6.Вычисление корня
    7.Синус
    8.Косинус
    9.Тангенс
    10.Выход
            """)
            s = input(">>>")
            run1 = True
            if "1" <= s <= "9":
                calc(s)
            elif s == "10":
                print("Выключение...")
                run = False
                run2 = False
            else:
                print("Введите заново!!")
                input()
    elif start == "2":
        print("Выключение...")
        run2 = False
    else:
        input()
        print("Введите заново!")
