print("""
████──███──████──█───██─███──███──████──██─██
█─────█────█──█──██─███─█─────█───█──█───███
█─██──███──█──█──█─█─██─███───█───████────█
█──█──█────█──█──█───██─█─────█───█─█─────█
████──███──████──█───██─███───█───█─█─────█
──────────────────────────────────────────█
""")

while True:
    print()
    menu = (input("""Выберите Действие:
     
    1 - Вычисление площади прямоугольника; 
    2 - Вычисление площади круга; 
    3 - Вычисление площади треугольника;
    4 - Вычисление площади трапеции;
    5 - Вычисление площади эллипса;
    6 - Вычисление площади ромба;
    7 - Вычисление площади параллелограмма;
    8 - Вычисление площади квадрата;
    9 - Вычисление площади четырехугольника;
    0 - Выход;
     
    Введите значение: """))
    print()
    import math

    if menu == "0":
        quit("Пока")

    elif menu == "1":
        while True:
            square = (input("""Введите формулу расчта: 
            1 - По двум сторонам;
            2 - По диагонали и углу;
            99- Выход в главное меню;
            0 - Выход; 
            
            Введите Значение: """))
            if square == "0":
                quit("Пока")
            elif square == "99":
                break
            elif square == "1":
                while True:
                    a = float(input("Введите длину: "))
                    b = float(input("Введите ширину: "))
                    s = a * b
                    print()
                    print(f"Площадь прямоугольника со сторонами {a} и {b} равна {s}")
                    menu_1 = (input("""Выберите действие:
             
    1 - Продолжить; 
    99- Главное меню; 
    0 - Выход;

    Введите значение: """))
                    if menu_1 == "1":
                        print()
                    elif menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
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
                    print("Площадь прямоугольника с диагональю {} и углом {} равна {}".format(d, s_in, s))
                    print()
                    menu_1 = (input("""Выберите действие: 
                1 - Продолжить;
                99 - Меню прямоугольника;
                0 - Выход;
                
                Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "2":
        while True:
            circle = (input("""Выберите формулу расчета: 
            1 - По радиусу; 
            2 - По диаметру; 
            3 - По длине окружности;
            99- Выход в главное меню;
            0 - Выход;
            
            Введите значение: """))
            if circle == "0":
                quit("Пока")
            elif circle == "99":
                break
                print()
            elif circle == "1":
                while True:
                    r = float(input("""
        Введите радиус: """))
                    print()
                    s = math.pi * r ** 2
                    print("""
Площадь круга с радиусом {} равна {}""".format(r, s))
                    print()
                    menu_1 = (input("""
    1 - Продолжить; 
    99- Меню окружности;
    0 - Выход;
    
    Введите значение: """))
                    print()
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

            elif circle == "2":
                while True:
                    print()
                    d = float(input("""Введите диаметр: """))
                    s = d ** 2 * math.pi / 4
                    print()
                    print("Площадь круга с диаметром {} равна {}".format(d, s))
                    print()
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню окружности;
                    0 - Выход;
                    
                    Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

            elif circle == "3":
                while True:
                    print()
                    length = float(input("""Введите длину окружности: """))
                    s = length ** 2 / 4 * math.pi
                    print()
                    print("Площадь круга с длиной окружности {} равна {}".format(length, s))
                    print()
                    menu_1 = (input("""
    1 - Продолжить;
    99- Меню окружности;
    0 - Выход;
    
    Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "3":
        while True:
            triangle = (input("""Выберите формулу расчёта:
         1 - По формуле Герона; 
         2 - По двум сторонам и углу между ними;
         3 - По стороне и опущенной на нее высоте;
         99- Выход в главное меню;
         0 - Выход;
         
          Введите значение: """))
            if triangle == "0":
                quit("Пока")
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
                    print("Площадь треугольника со сторонами {}, {} и {} равна {}".format(a, b, c, s))
                    print()
                    menu_1 = (input("""
                    1 - Продолжить; 
                    99- Меню треугольника;
                    0 - Выход;
                    
                    Введите значение: """))
                    print()
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
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
                    print("Площадь треугольника со сторонами {}, {}, и углом {} равна {}".format(a, b, s_in, s))
                    print()
                    menu_1 = (input("""
                    1 - Продолжить; 
                    99-Меню треугольника;
                    0-Выход;
                    
                    Введите значение: """))
                    print()
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

            elif triangle == "3":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    h = float(input("""Введите длину высоты: """))
                    s = a * h / 2
                    print()
                    print("Площадь треугольника со стороной {} и высотой {} равна {}".format(a, h, s))
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню треугольника;
                    0 - Выход;
                    
                    Введите значение: """))
                    print()
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "4":
        while True:
            trapeze = (input("""Выберите формулу расчета: 
            1 - По двум основаниям и высоте; 
            2 - По средней линии и высоте;
            3 - По диагоналям и углу между ними;
            99- В главное меню;
            0 - Выход;
            
            Введите значение: """))
            if trapeze == "0":
                quit("Пока")
            elif trapeze == "99":
                break
            elif trapeze == "1":
                while True:
                    a = float(input("""Введите длину первого основания: """))
                    b = float(input("""Введите длину второго основания: """))
                    h = float(input("""Введите высоту: """))
                    s = ((a + b) / 2) * h
                    print("Площадь трапеции с основаниями {}, {} и высотой {} равна {}".format(a, b, h, s))
                    menu_1 = (input("""
                1 - Продолжить;
                99- Меню трапеции;
                0 - Выход;
                
                Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

            elif trapeze == "2":
                while True:
                    m = float(input("""Введите среднюю линию: """))
                    h = float(input("""Введите высоту: """))
                    s = m * h
                    print("Площадь трапеции с высотой {} и средней линией {} равна {}".format(h, m, s))
                    menu_1 = (input("""
                1 - Продолжить;
                99- Меню трапеции
                0 - Выход;
                
                Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
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
                    print("Площадь трапеции с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    menu_1 = (input("""
                1 - Продолжить;
                99- Меню трапеции;
                0 - Выход;
                
                Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "5":
        while True:
            circle = (input("""
            1 - По длине полуосей;
            99- В главное меню; 
            0 - Выход;
            
            Введите значение: """))
            if circle == "0":
                quit("Пока")
            elif circle == "99":
                break
            elif circle == "1":
                while True:
                    a = float(input("""Введите большую полуось: """))
                    b = float(input("""Введите малую полуось: """))
                    s = math.pi * a * b
                    print("Площадь эллипса с полуосями {} и {} равна {}".format(a, b, s))
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню эллипса;
                    0 - Выход;
                    
                    Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "6":
        while True:
            rhombus = (input("""Введите формулу расчёта: 
            1 - По длинам основания и высоты ромба; 
            2 - По длинам диагоналей;
            3 - По стороне и углу;
            99- В главное меню; 
            0 - Выход;
            
            Введите значение: """))
            if rhombus == "0":
                quit("Пока")
            elif rhombus == "99":
                break
            elif rhombus == "1":
                while True:
                    a = float(input("""Введите длину основания: """))
                    h = float(input("""Введите высоту: """))
                    s = a * h
                    print("Площадь ромба с основанием {} и высотой {} равна {}".format(a, h, s))
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню ромба;
                    0 - Выход;
                    
                    Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

            elif rhombus == "2":
                while True:
                    d_1 = float(input("""Введите длину первой диагонали: """))
                    d_2 = float(input("""Введите длину второй диагонали: """))
                    s = d_1 * d_2 / 2
                    print("Площадь ромба с диагоналми {} и {} равна {}".format(d_1, d_2, s))
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню ромба;
                    0 - Выход: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
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
                    print("Площадь ромба со стороной {} и углом {} равна {}".format(a, s_in, s))
                    menu_1 = (input("""
                    1 - Продолжить;
                    99- Меню ромба;
                    0 - Выход;
                    
                    Введите значение: """))
                    if menu_1 == "0":
                        quit("Пока")
                    elif menu_1 == "1":
                        print()
                    else:
                        break

    elif menu == "7":
        while True:
            menu_1 = (input("""Выберите формулу расчета:
            1 - По двум сторонам и углу между ними;
            2 - По стороне и высоте;
            3 - По диагоналям и углу;
            99- Главное меню;
            0 - Выход;
            
            Введите значение: """))
            if menu_1 == "0":
                quit("Пока")
            elif menu_1 == "99":
                break
            elif menu_1 == "1":
                while True:
                    a = float(input("Введите сторону: "))
                    b = float(input("Введите сторону: "))
                    s_in = float(input("Введите угол: "))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a * b * x
                    print("Площадь параллелограмма со сторонами {}, {} и углом {} равна {}".format(a, b, s_in, s))
                    par = (input("""
                        1 - Продолжить;
                        99- Меню параллелограмма;
                        0 - Выход;
                        
                        Введите значение: """))
                    if par == "0":
                        quit("Пока")
                    elif par == "1":
                        print()
                    else:
                        break

            elif menu_1 == "2":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    h = float(input("""Введите высоту: """))
                    s = a * h
                    print("Площадь параллелограмма со стороной {} и высотой {} равна {}".format(a, h, s))
                    par = (input("""
                        1 - Продолжить;
                        99- Меню параллелограмма;
                        0 - Выход;
                        
                        Введите значение: """))
                    if par == "0":
                        quit("Пока")
                    elif par == "1":
                        print()
                    else:
                        break
            elif menu_1 == "3":
                while True:
                    d1 = float(input("""Введите диагональ: """))
                    d2 = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print("Площадь параллелограмма с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    par = (input("""
                    1 - Продолжить;
                    99- Меню параллелограмма;
                    0 - Выход;
                    
                    Введите значение: """))
                    if par == "0":
                        quit("Пока")
                    elif par == "1":
                        print()
                    else:
                        break

    elif menu == "8":
        while True:
            menu_1 = (input("""Выберите формулу расчета:
             1 - По стороне;
             2 - По диагонали;
             99- Главное меню;
             0 - Выход;
             
             Введите значение: """))
            if menu_1 == "0":
                quit("Пока")
            elif menu_1 == "99":
                break
            elif menu_1 == "1":
                while True:
                    a = float(input("""Введите длину стороны: """))
                    s = a ** 2
                    print("Площадь квадрата со стороной {} равна {}".format(a, s))
                    square = (input("""
                1 - Продолжить;
                99- Меню квадрата;
                0 - Выход;
                
                Введите значение: """))
                    if square == "0":
                        quit("Пока")
                    elif square == "1":
                        print()
                    else:
                        break

            elif menu_1 == "2":
                while True:
                    d = float(input("""Введите диагональ: """))
                    s = d ** 2 / 2
                    print("Площадь квадрата с диагональю {} равна {}".format(d, s))
                    square = (input("""
                1 - Продолжить;
                99- Меню квадрата;
                0 - Выход;
                
                Введите значение: """))
                    if square == "0":
                        quit("Пока")
                    elif square == "1":
                        print()
                    else:
                        break

    elif menu == "9":
        while True:
            menu_1 = (input("""Введите формулу расчета:
            1 - По длине диагоналей и углу между ними;
            2 - По длине сторон и два противоположных угла (В разработке);
            3 - По полупериметру и радиусу вписанной окружности;
            99- Главное меню;
            0 - Выход;
            
            Введите значение: """))
            if menu_1 == "0":
                quit("Пока")
            elif menu_1 == "99":
                break
            elif menu_1 == "1":
                while True:
                    d1 = float(input("""Введите диагональ: """))
                    d2 = float(input("""Введите диагональ: """))
                    s_in = float(input("""Введите угол: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print("Площадь четыреугольника с диагоналями {}, {} и углом {} равна {}".format(d1, d2, s_in, s))
                    quadra = (input("""
                    1 - Продолжить;
                    99- В меню четырехугольника;
                    0 - Выход;
                    
                    Введите значение: """))
                    if quadra == "0":
                        quit("Пока")
                    elif quadra == "1":
                        print()
                    else:
                        break

            elif menu_1 == "2":
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
                    print("""В разработке""")
                    break
            elif menu_1 == "3":
                while True:
                    p = float(input("""Введите полупериметр: """))
                    r = float(input("""Введите радиус: """))
                    s = p * r
                    print("Площадь четырехугольника с полупериметром {} и окружностью {} равна {}".format(p, r, s))
                    quadra = (input("""
                    1 - Продолжить;
                    99- В меню четырехугольника;
                    0 - Выход;
                    
                    Введите значение: """))
                    if quadra == "0":
                        quit("Пока")
                    elif quadra == "1":
                        print()
                    else:
                        break
