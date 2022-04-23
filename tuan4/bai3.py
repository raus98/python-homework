def tinhTienCuoc():
    s = 25000
    a = int(input("Nhap so phut da goi: "))
    if a <= 50:
        s += 600*a
    elif 50 < a <= 200:
        s += 600*50 + (a - 50)*400
    else:
        s += 600*50 + 400*150 + (a - 200)*200
    return print("Tien cuoc dien thoai la: " + str(s) + "vnd")