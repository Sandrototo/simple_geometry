import math
import func_tion


while True:
    print()
    menu = input(func_tion.en_menu())
    print()

    if menu == "0":
        func_tion.quit_1()

    elif menu == "1":
        while True:
            square = input(func_tion.en_square())
            if square == "0":
                func_tion.quit_1()
            elif square == "99":
                break
            elif square == "1":
                while True:
                    a = float(input("Enter length: "))
                    b = float(input("Enter the streak: "))
                    s = a * b
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a rectangle with sides {a} and {b} is equal to {s}")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif square == "2":
                while True:
                    d = float(input("""Enter the diagonal: """))
                    s_in = float(input("""Enter the angle: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d ** 2 * x / 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​the rectangle with diagonal {} and angle {} is {}".format(d, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "2":
        while True:
            circle = input(func_tion.en_circle())
            if circle == "0":
                func_tion.quit_1()
            elif circle == "99":
                break
                print()
            elif circle == "1":
                while True:
                    r = float(input("""
        Enter radius: """))
                    print()
                    s = math.pi * r ** 2
                    l1 = 2 * math.pi * r
                    print(func_tion.line("-", 100))
                    print(f"""
The area of ​​a circle with radius {r} is equal to {s} and the circumference is equal to {l1}""")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif circle == "2":
                while True:
                    print()
                    d = float(input("""Enter diameter: """))
                    s = d ** 2 * math.pi / 4
                    print(func_tion.line("-", 100))
                    print("The area of ​​a circle with diameter {} is equal to {}".format(d, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif circle == "3":
                while True:
                    print()
                    length = float(input("""Enter the circumference: """))
                    s = length ** 2 / 4 * math.pi
                    print(func_tion.line("-", 100))
                    print("he area of ​​a circle with a circumference of {} is equal to {}".format(length, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "3":
        while True:
            triangle = input(func_tion.en_triangle())
            if triangle == "0":
                func_tion.quit_1()
            elif triangle == "99":
                break
            elif triangle == "1":
                while True:
                    a = float(input("""Enter side: """))
                    b = float(input("Enter side: "))
                    c = float(input("Enter side: "))
                    p = (a + b + c) / 2
                    s_1 = (p - a) * (p - b) * (p - c)
                    s_2 = p * s_1
                    s = s_2 ** 0.5
                    print(func_tion.line("-", 100))
                    print("The area of ​​a triangle with sides {}, {} and {} is {}".format(a, b, c, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif triangle == "2":
                while True:
                    a = float(input("""Enter side: """))
                    b = float(input("Enter side: "))
                    s_in = float(input("Enter the angle: "))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a * b * x / 2
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a triangle with sides {a}, {b}, and angle {s_in} is equal to {s}")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif triangle == "3":
                while True:
                    a = float(input("""Enter side length: """))
                    h = float(input("""Enter the length of the height: """))
                    s = a * h / 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​a triangle with side {} and height {} is {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "4":
        while True:
            trapeze = input(func_tion.en_trapeze())
            if trapeze == "0":
                func_tion.quit_1()
            elif trapeze == "99":
                break
            elif trapeze == "1":
                while True:
                    a = float(input("""Enter the length of the first base: """))
                    b = float(input("""Enter the length of the second base: """))
                    h = float(input("""Enter height: """))
                    s = ((a + b) / 2) * h
                    print(func_tion.line("-", 100))
                    print("The area of ​​a trapezoid with bases {}, {} and height {} is {}".format(a, b, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif trapeze == "2":
                while True:
                    m = float(input("""Enter the middle line: """))
                    h = float(input("""Enter height: """))
                    s = m * h
                    print(func_tion.line("-", 100))
                    print("The area of ​​a trapezoid with height {} and midline {} is equal to {}".format(h, m, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif trapeze == "3":
                while True:
                    d1 = float(input("""Enter the diagonal: """))
                    d2 = float(input("""Enter the diagonal: """))
                    s_in = float(input("""Enter the angle: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​a trapezoid with diagonals {}, {} and angle {} is {}".format(d1, d2, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "5":
        while True:
            circle = input(func_tion.en_circle_2())
            if circle == "0":
                func_tion.quit_1()
            elif circle == "99":
                break
            elif circle == "1":
                while True:
                    a = float(input("""Enter semi-major axis: """))
                    b = float(input("""Enter the semi-minor axis: """))
                    s = math.pi * a * b
                    print(func_tion.line("-", 100))
                    print("The area of ​​an ellipse with semi-axes {} and {} is equal to {}".format(a, b, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "6":
        while True:
            rhombus = input(func_tion.en_rhombus())
            if rhombus == "0":
                func_tion.quit_1()
            elif rhombus == "99":
                break
            elif rhombus == "1":
                while True:
                    a = float(input("""Enter base length: """))
                    h = float(input("""Enter height: """))
                    s = a * h
                    print(func_tion.line("-", 100))
                    print("The area of ​​a rhombus with base {} and height {} is {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rhombus == "2":
                while True:
                    d_1 = float(input("""Enter the length of the first diagonal: """))
                    d_2 = float(input("""Enter the length of the second diagonal: """))
                    s = d_1 * d_2 / 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​a rhombus with diagonals {} and {} is equal to {}".format(d_1, d_2, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            if rhombus == "3":
                while True:
                    a = float(input("""Enter side length: """))
                    s_in = float(input("""Enter the angle: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a ** 2 * x
                    print(func_tion.line("-", 100))
                    print("The area of ​​a rhombus with side {} and angle {} is equal to {}".format(a, s_in, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "7":
        while True:
            par = input(func_tion.en_par())
            if par == "0":
                func_tion.quit_1()
            elif par == "99":
                break
            elif par == "1":
                while True:
                    a = float(input("Enter side: "))
                    b = float(input("Enter side: "))
                    s_in = float(input("Enter the angle: "))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = a * b * x
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a parallelogram with sides {a}, {b} and angle {s_in} is equal to {s}""")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif par == "2":
                while True:
                    a = float(input("""Enter side length: """))
                    h = float(input("""Enter height: """))
                    s = a * h
                    print(func_tion.line("-", 100))
                    print("The area of ​​a parallelogram with side {} and height {} is equal to {}".format(a, h, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif par == "3":
                while True:
                    d1 = float(input("""Enter the diagonal: """))
                    d2 = float(input("""Enter the diagonal: """))
                    s_in = float(input("""Enter the angle: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a parallelogram with the diagonals {d1}, {d2} and the angle {s_in} is {s}")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "8":
        while True:
            square = input(func_tion.en_square_2())
            if square == "0":
                func_tion.quit_1()
            elif square == "99":
                break
            elif square == "1":
                while True:
                    a = float(input("""Enter side length: """))
                    s = a ** 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​a square with side {} is equal to {}".format(a, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif square == "2":
                while True:
                    d = float(input("""Enter the diagonal: """))
                    s = d ** 2 / 2
                    print(func_tion.line("-", 100))
                    print("The area of ​​the square with the diagonal {} is {}".format(d, s))
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

    elif menu == "9":
        while True:
            rectangle = input(func_tion.en_rectangle())
            if rectangle == "0":
                func_tion.quit_1()
            elif rectangle == "99":
                break
            elif rectangle == "1":
                while True:
                    d1 = float(input("""Enter the diagonal: """))
                    d2 = float(input("""Enter the diagonal: """))
                    s_in = float(input("""Enter the angle: """))
                    angle = s_in * math.pi
                    angle = angle / 180
                    x = (math.sin(angle))
                    s = d1 * d2 * x / 2
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a quadrilateral with diagonals {d1}, {d2} and an angle {s_in} is {s}")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rectangle == "2":
                while True:
                    a = float(input("""Enter side length: """))
                    b = float(input("""Enter side length: """))
                    c = float(input("""Enter side length: """))
                    d = float(input("""Enter side length: """))
                    angle_1 = float(input("""Enter the angle: """))
                    angle_2 = float(input("""Enter the angle: """))
                    rad_angle_1 = math.radians(angle_1)
                    rad_angle_2 = math.radians(angle_2)
                    cos_angle = math.cos((rad_angle_1 + rad_angle_2) / 2)
                    res_cos = math.pow(cos_angle, 2)
                    res1 = res_cos * a * b * c * d
                    res2 = (a + b + c + d) / 2
                    res3 = (res2 - a) * (res2 - b) * (res2 - c) * (res2 - d)
                    res4 = res3 - res1
                    result = math.sqrt(res4)
                    print(func_tion.line("-", 100))
                    print(f"""
The area of ​​a quadrilateral with sides {a}, {b}, {c}, {d} and angles {angle_1} and {angle_2} is {result}""")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rectangle == "3":
                while True:
                    p = float(input("""Enter semi-perimeter: """))
                    r = float(input("""Enter radius: """))
                    s = p * r
                    print(func_tion.line("-", 100))
                    print(f"The area of ​​a quadrilateral with a semiperimeter {p} and a circle {r} is equal to {s}")
                    print(func_tion.line("-", 100))
                    func_tion.en_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break

            elif rectangle == "4":
                while True:
                    a = float(input("Enter side(a): "))
                    b = float(input("Enter side(b): "))
                    c = float(input("Enter side(c): "))
                    d = float(input("Enter side(d): "))
                    dia_1 = float(input("Enter 1 diagonal: "))
                    dia_2 = float(input("Enter 2 diagonal: "))
                    s = (a + b + c + d) / 2
                    rres = (a * c + b * d + dia_1 * dia_2) * (a * c + b * d - dia_1 * dia_2) * 0.25
                    lres = (s - a) * (s - b) * (s - c) * (s - d)
                    res = lres - rres
                    result = math.sqrt(res)
                    print(func_tion.line("-", 100))
                    print(f"""
The area of ​​a quadrilateral with sides {a}, {b}, {c}, {d} and diagonals {dia_1} and {dia_2} is {result}""")
                    print(func_tion.line("-", 100))
                    func_tion.rus_func()
                    if func_tion.result[0] == "99":
                        break
                else:
                    break
