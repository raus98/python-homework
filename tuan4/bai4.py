def tinhTongSoNguyenDuong():
    i = 0
    s = 0
    n = int(input("Nhap n: "))
    while i <= n:
        s += i
        i += 1
    return print("Tong S = " + str(s))
