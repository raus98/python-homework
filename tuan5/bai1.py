def nhapMang():
    n = int(input("Nhap n: "))
    a = []
    for i in range(1, n + 1):
        a.append(int(input("Nhap so nguyen thu " + str(i) + ": ")))
    return a

def findMax():
    a = nhapMang()
    a.sort()
    return print("So lon nhat la: " + str(a[-1]))

def findTheSecondMax():
    a = nhapMang()
    a.sort()
    return print("So lon nhi: " + str(a[len(a) - a.count(max(a)) - 1]))

def kiemTraDoiXung():
    a = nhapMang()
    i = 0
    n = int(len(a) / 2)
    for i in range(0, n):
        if a[i] != a[len(a) - i - 1]:
            return print("Mang khong doi xung")
    return print("Mang doi xung")

def tinhTongCacSoNguyenTo():
    a = nhapMang()
    S = 0
    temp = 0
    for i in a:
        if i == 2:
            S += i
        else:
            for n in range(2, i):
                if i % n == 0:
                    temp = 0
                    break
                else:
                    temp = i
            S += temp
            temp = 0
    return print("Tong cac so nguyen to: " + str(S))

def cacPhanTuLonHonX():
    a = nhapMang()
    x = int(input("Nhap x: "))
    xyz = []
    for i in a:
        if i > x and i not in xyz:
            xyz.append(i)
    return print("Cac phan tu lon hon X: " + str(xyz))

def sapXepMangTangDan():
    a = nhapMang()
    a.sort()
    return print("Sap xep mang tang dan: " + str(a))

def tanSuatXuatHien():
    a = nhapMang()
    xyz = []
    for i in a:
        if i not in xyz:
            xyz.append(i)
            print("So lan xuat hien cua " + str(i) + " la: " + str(a.count(i)))
    return 0
