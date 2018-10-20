import math
run1 = 0
def search(x):
    tt = True
    if tt == x.isdigit():
        x = float(x)
        global run1
        run1 = False
        return x
run = True
while run:
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
8.Выход
            """)
            s = input(">>>")
            run1 = True
            if s == "1":
                while run1:
                    a = input("Введите первое число: ")
                    search(a)
                run1 = True
                while run1:
                    b = input("Введите второе число: ")
                    search(b)
                a = float(a)
                b = float(b)
                print(a + b)
                continue
            elif s == "2":
                while run1:
                    a = input("Введите первое число: ")
                    search(a)
                run1 = True
                while run1:
                    b = input("Введите второе число: ")
                    search(b)
                a = float(a)
                b = float(b)
                print(a - b)
                continue
            elif s == "3":
                while run1:
                    a = input("Введите первое число: ")
                    search(a)
                run1 = True
                while run1:
                    b = input("Введите второе число: ")
                    if b == "0":
                        print("Некорректный ввод!!")
                        continue
                    else:
                        search(b)
                a = float(a)
                b = float(b)
                print(a / b)
                continue
            elif s == "4":
                while run1:
                    a = input("Введите первое число: ")
                    search(a)
                run1 = True
                while run1:
                    b = input("Введите второе число: ")
                    search(b)
                a = float(a)
                b = float(b)
                print(a * b)
                continue
            elif s == "5":
                while run1:
                    while run1:
                        a = input("Введите число: ")
                        search(a)
                    run1 = True
                    while run1:
                        b = input("Введите степень: ")
                        search(b)
                    a = float(a)
                    b = float(b)
                print(a ** b)
                continue
            elif s == "6":
                while run1:
                    a = input("Введите число под корнем: ")
                    search(a)
                a = float(a)
                print(a ** 0.5)
                continue
            elif s == "7":
                while run1:
                    while run1:
                        a = input("Введите синус какого числа ищем: ")
                        search(a)
                    a = float(a)
                print(math.sin(a))
                continue
            elif s == "8":
                print("Выключение...")
                run = False
            else:
                print("Введите заново!!")
                continue
    elif start == "2":
        print("Выключение...")
        run = False
    else:
        print("Введите заново!")