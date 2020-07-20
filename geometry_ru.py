import math
import func_tion


while True:
    print()
    menu = input(func_tion.rus_menu())
    print()

    if menu == "0":
        func_tion.quit_1()

    elif menu == "1":
        while True:
            square = input(func_tion.rus_square())
            if square == "0":
                func_tion.quit_1()
            elif square == "99":
                break
            elif square == "1":
                while True:
                    a = float(input("Введите длину: "))
                    b = float(input("Введите ширину: "))
                    s = a * b
                    print(func_tion.line("-", 100))
                    print(f"Площадь прямоугольника со сторонами {a} и {b} равна {s}")
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif square == "2":
                while True:
                    d = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d ** 2 * x / 2
                    print(func_tion.line("-", 100))
                    print("Площадь прямоугольника с диагональю {} и углом {} равна {}".format(d, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "2":
        while True:
            circle = input(func_tion.rus_circle())
            if circle == "0":
                func_tion.quit_1()
            elif circle == "99":
                break
                print()
            elif circle == "1":
                while True:
                    r = float(input("""
        Введите радиус: """))
                    print()
                    s = math.pi * r ** 2
                    print(func_tion.line("-", 100))
                    print("""
Площадь круга с радиусом {} равна {}""".format(r, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif circle == "2":
                while True:
                    print()
                    d = float(input("""Введите диаметр: """))
                    s = d ** 2 * math.pi / 4
                    print(func_tion.line("-", 100))
                    print("Площадь круга с диаметром {} равна {}".format(d, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif circle == "3":
                while True:
                    print()
                    length = float(input("""Введите длину окружности: """))
                    s = length ** 2 / 4 * math.pi
                    print(func_tion.line("-", 100))
                    print("Площадь круга с длиной окружности {} равна {}".format(length, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "3":
        while True:
            triangle = input(func_tion.rus_triangle())
            if triangle == "0":
                func_tion.quit_1()
            elif triangle == "99":
                break
            elif triangle == "1":
                while True:
                    a = float(input("""Введите сторону: """))
                    b = float(input("Введите сторону: "))
                    c = float(input("Введите сторону: "))
                    p = (a + b + c) / 2
                    s_1 = (p - a) * (p - b) * (p - c)
                    s_2 = p * s_1
                    s = s_2 ** 0.5
                    print(func_tion.line("-", 100))
                    print("Площадь треугольника со сторонами {}, {} и {} равна {}".format(a, b, c, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif triangle == "2":
                while True:
                    a = float(input("""Введите сторону: """))
                    b = float(input("Введите сторону: "))
                    s_in = float(input("Введите угол: "))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a * b * x / 2
                    print(func_tion.line("-", 100))
                    print("Площадь треугольника со сторонами {}, {}, и углом {} равна {}".format(a, b, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif triangle == "3":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    h = float(input("""Введите длину высоты: """))
                    s = a * h / 2
                    print(func_tion.line("-", 100))
                    print("Площадь треугольника со стороной {} и высотой {} равна {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "4":
        while True:
            trapeze = input(func_tion.rus_trapeze())
            if trapeze == "0":
                func_tion.quit_1()
            elif trapeze == "99":
                break
            elif trapeze == "1":
                while True:
                    a = float(input("""Введите длину первого основания: """))
                    b = float(input("""Введите длину второго основания: """))
                    h = float(input("""Введите высоту: """))
                    s = ((a + b) / 2) * h
                    print(func_tion.line("-", 100))
                    print("Площадь трапеции с основаниями {}, {} и высотой {} равна {}".format(a, b, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif trapeze == "2":
                while True:
                    m = float(input("""Введите среднюю линию: """))
                    h = float(input("""Введите высоту: """))
                    s = m * h
                    print(func_tion.line("-", 100))
                    print("Площадь трапеции с высотой {} и средней линией {} равна {}".format(h, m, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif trapeze == "3":
                while True:
                    d1 = float(input("""Введите диагональ: """))
                    d2 = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print("Площадь трапеции с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "5":
        while True:
            circle = input(func_tion.rus_circle_2())
            if circle == "0":
                func_tion.quit_1()
            elif circle == "99":
                break
            elif circle == "1":
                while True:
                    a = float(input("""Введите большую полуось: """))
                    b = float(input("""Введите малую полуось: """))
                    s = math.pi * a * b
                    print(func_tion.line("-", 100))
                    print("Площадь эллипса с полуосями {} и {} равна {}".format(a, b, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "6":
        while True:
            rhombus = input(func_tion.rus_rhombus())
            if rhombus == "0":
                func_tion.quit_1()
            elif rhombus == "99":
                break
            elif rhombus == "1":
                while True:
                    a = float(input("""Введите длину основания: """))
                    h = float(input("""Введите высоту: """))
                    s = a * h
                    print(func_tion.line("-", 100))
                    print("Площадь ромба с основанием {} и высотой {} равна {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rhombus == "2":
                while True:
                    d_1 = float(input("""Введите длину первой диагонали: """))
                    d_2 = float(input("""Введите длину второй диагонали: """))
                    s = d_1 * d_2 / 2
                    print(func_tion.line("-", 100))
                    print("Площадь ромба с диагоналми {} и {} равна {}".format(d_1, d_2, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            if rhombus == "3":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a ** 2 * x
                    print(func_tion.line("-", 100))
                    print("Площадь ромба со стороной {} и углом {} равна {}".format(a, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "7":
        while True:
            par = input(func_tion.rus_par())
            if par == "0":
                func_tion.quit_1()
            elif par == "99":
                break
            elif par == "1":
                while True:
                    a = float(input("Введите сторону: "))
                    b = float(input("Введите сторону: "))
                    s_in = float(input("Введите угол: "))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a * b * x
                    print(func_tion.line("-", 100))
                    print("Площадь параллелограмма со сторонами {}, {} и углом {} равна {}".format(a, b, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif par == "2":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    h = float(input("""Введите высоту: """))
                    s = a * h
                    print(func_tion.line("-", 100))
                    print("Площадь параллелограмма со стороной {} и высотой {} равна {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif par == "3":
                while True:
                    d1 = float(input("""Введите диагональ: """))
                    d2 = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print("Площадь параллелограмма с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "8":
        while True:
            square = input(func_tion.rus_square_2())
            if square == "0":
                func_tion.quit_1()
            elif square == "99":
                break
            elif square == "1":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    s = a ** 2
                    print(func_tion.line("-", 100))
                    print("Площадь квадрата со стороной {} равна {}".format(a, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif square == "2":
                while True:
                    d = float(input("""Введите диагональ: """))
                    s = d ** 2 / 2
                    print(func_tion.line("-", 100))
                    print("Площадь квадрата с диагональю {} равна {}".format(d, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "9":
        while True:
            rectangle = input(func_tion.rus_rectangle())
            if rectangle == "0":
                func_tion.quit_1()
            elif rectangle == "99":
                break
            elif rectangle == "1":
                while True:
                    d1 = float(input("""Введите диагональ: """))
                    d2 = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print("Площадь четыреугольника с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rectangle == "2":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    b = float(input("""Введите длину стороны: """))
                    c = float(input("""Введите длину стороны: """))
                    d = float(input("""Введите длину стороны: """))
                    s_in1 = float(input("""Введите угол: """))
                    s_in2 = float(input("""Введите угол: """))
                    angle1 = s_in1 * math.pi
                    angle1 = angle1 / 180
                    x1 = (math.sin(angle1))
                    angle2 = s_in2 * math.pi
                    angle2 = angle2 / 180
                    x2 = (math.sin(angle2))
                    p = (a + b + c + d) / 2
                    o = (x1 + x2) / 2
                    print(line("-", 100))
                    print("""В разработке""")
                    print(line("-", 100))
                    break
            elif rectangle == "3":
                while True:
                    p = float(input("""Введите полупериметр: """))
                    r = float(input("""Введите радиус: """))
                    s = p * r
                    print(func_tion.line("-", 100))
                    print("""Площадь четырехугольника с полупериметром {} и окружностью {} равна {}""".format(p, r, s))
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break
