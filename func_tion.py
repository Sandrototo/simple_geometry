esult = []


def line(sep, sep_len):
    return sep * sep_len


def rus_func():
    while True:
        result.clear()
        menu_1 = (input("""
                1 - Продолжить;
                99- Меню;
                0 - Выход;

                Введите значение: """))
        if menu_1 == "0":
            quit_1()
        elif menu_1 == "1":
            result.append(menu_1)
            break
        elif menu_1 == "99":
            result.append(menu_1)
            break


def quit_1():
    quit(""" 
    ██████████████████████████████████████████
    █────██────██────██────███────███─█─██───█
    █─█████─██─██─██─██─██──██─██──██─█─██─███
    █─█──██─██─██─██─██─██──██────███─█─██───█
    █─██─██─██─██─██─██─██──██─██──██─█─██─███
    █────██────██────██────███────███───██───█
    ██████████████████████████████████████████""")


def rus_menu():
    menu = ("""Выберите Действие:

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

        Введите значение: """)
    return menu


def rus_square():
    square = ("""Введите формулу расчта: 
                1 - По двум сторонам;
                2 - По диагонали и углу;
                99- Выход в главное меню;
                0 - Выход; 

                Введите Значение: """)
    return square


def rus_circle():
    circle = ("""Выберите формулу расчета: 
                1 - По радиусу; 
                2 - По диаметру; 
                3 - По длине окружности;
                99- Выход в главное меню;
                0 - Выход;

                Введите значение: """)
    return circle


def rus_triangle():
    triangle = ("""Выберите формулу расчёта:
             1 - По формуле Герона; 
             2 - По двум сторонам и углу между ними;
             3 - По стороне и опущенной на нее высоте;
             99- Выход в главное меню;
             0 - Выход;

              Введите значение: """)
    return triangle


def rus_trapeze():
    trapeze = ("""Выберите формулу расчета: 
               1 - По двум основаниям и высоте; 
               2 - По средней линии и высоте;
               3 - По диагоналям и углу между ними;
               99- В главное меню;
               0 - Выход;

               Введите значение: """)
    return trapeze


def rus_circle_2():
    circle = ("""
                1 - По длине полуосей;
                99- В главное меню; 
                0 - Выход;

                Введите значение: """)
    return circle


def rus_rhombus():
    rhombus = ("""Введите формулу расчёта: 
                1 - По длинам основания и высоты ромба; 
                2 - По длинам диагоналей;
                3 - По стороне и углу;
                99- В главное меню; 
                0 - Выход;

                Введите значение: """)
    return rhombus


def rus_par():
    par = ("""Выберите формулу расчета:
                1 - По двум сторонам и углу между ними;
                2 - По стороне и высоте;
                3 - По диагоналям и углу;
                99- Главное меню;
                0 - Выход;

                Введите значение: """)
    return par


def rus_square_2():
    square = ("""Выберите формулу расчета:
                 1 - По стороне;
                 2 - По диагонали;
                 99- Главное меню;
                 0 - Выход;

                 Введите значение: """)
    return square


def rus_rectangle():
    rectangle = ("""
        Введите формулу расчета:
        1 - По длине диагоналей и углу между ними;
        2 - По длине сторон и два противоположных угла;
        3 - По полупериметру и радиусу вписанной окружности;
        4 - По длинам четырех сторон и диагоналям;
        99- Главное меню;
        0 - Выход;

        Введите значение: """)
    return rectangle


def en_menu():
    menu = """Choose an action:
    1 - Area of ​​the rectangle;
    2 - Area of ​​a circle;
    3 - the area of ​​the triangle;
    4 - the area of ​​the trapezoid;
    5 - the area of ​​the ellipse;
    6 - Area of ​​a rhombus;
    7 - Area of ​​a parallelogram;
    8 - Square area;
    9 - Area of ​​a quadrangle;
    0 - Exit;

    Enter value: """
    return menu


def en_func():
    while True:
        result.clear()
        menu_1 = (input("""
                1 - Proceed;
                99- Menu;
                0 - Exit;

                Enter the value: """))
        if menu_1 == "0":
            quit_1()
        elif menu_1 == "1":
            result.append(menu_1)
            break
        elif menu_1 == "99":
            result.append(menu_1)
            break


def en_square():
    square = ("""Enter the calculation formula: 
                1 - On two sides;
                2 - Diagonal and corner;
                99- Exit to the main menu;
                0 - Exit; 

                Enter value: """)
    return square


def en_circle():
    circle = ("""Select a calculation formula: 
                1 - Radius; 
                2 - By diameter; 
                3 - Along the circumference;
                99- Exit to the main menu;
                0 - Exit;

                Enter value: """)
    return circle


def en_triangle():
    triangle = ("""Select calculation formula:
             1 - According to Heron's formula; 
             2 - On two sides and the corner between them;
             3 - Along the side and the height lowered on it;
             99- Exit to the main menu;
             0 - Exit;

              Enter value: """)
    return triangle


def en_trapeze():
    trapeze = ("""Select a calculation formula: 
               1 - On two bases and height; 
               2 - About midline and height;
               3 - Diagonals and the angle between them;
               99- Exit to the main menu;
               0 - Exit;

               Enter value: """)
    return trapeze


def en_circle_2():
    circle = ("""
                1 - Along the length of the semiaxes;
                99- To the main menu; 
                0 - Exit;

                Enter value: """)
    return circle


def en_rhombus():
    rhombus = ("""Enter the calculation formula: 
                1 - By base length and rhombus height; 
                2 - By the lengths of the diagonals;
                3 - By side and corner;
                99- To the main menu; 
                0 - Exit;

                Enter value: """)
    return rhombus


def en_par():
    par = ("""Select a calculation formula:
                1 - On two sides and the corner between them;
                2 - By side and height;
                3 - Diagonally and corner;
                99- Main menu;
                0 - Exit;

                Enter value: """)
    return par


def en_square_2():
    square = ("""Select a calculation formula:
                 1 - By side;
                 2 - Diagonally;
                 99- Main menu;
                 0 - Exit;

                 Enter value: """)
    return square


def en_rectangle():
    rectangle = ("""
        Enter the calculation formula:
        1 - Along the length of the diagonals and the angle between them;
        2 - Along the length of the sides and two opposite corners;
        3 - Half-perimeter and inscribed circle radius;
        4 - By the lengths of the four sides and diagonals;
        99- Main menu;
        0 - Exit;

        Enter value: """)
    return rectangle
