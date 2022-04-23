def xepHangHocLuc():
    a = int(input("Nhap diem giua ky: "))
    b = int(input("Nhap diem thi cuoi ky: "))
    dtb = (a + b)/2
    if dtb >= 9:
        return print("Hang A")
    elif 7 <= dtb < 9:
        return print("Hang B")
    elif 5 <= dtb < 7:
        return print("Hang C")
    else:
        print("Hang F")
    return 0
