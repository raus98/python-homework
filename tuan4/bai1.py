import math
def giaiPhuongTrinhBac2():
    print("ax^2 + bx + c = 0 (a khac 0)")
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        return print("Phuong trinh vo nghiem")
    elif delta == 0:
        return print("Phuong trinh co nghiem kep: x1 = x2 = " + str(-b/(2*a)))
    else:
        print("Phuong trinh co 2 nghiem phan biet:")
        print("x1 = " + str((-b + math.sqrt(delta))/(2*a)))
        print("x1 = " + str((-b - math.sqrt(delta)) / (2 * a)))
    return 0

