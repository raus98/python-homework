def tinhTong():
    n = int(input("Nhap n: "))
    soLe = 0
    s = 0
    for i in range(0, n + 1):
        soLe += 2*i + 1
        s += 1/soLe
    return print("S = " + str(s))
