import math
def nhapSoNguyenDuong():
    n = int(input("Nhap so nguyen duong n: "))
    return n

def tongCacSoLeNhoHonN():
    n = nhapSoNguyenDuong()
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
    return print("Tong cac so le nho hon " + str(n) + " la: " + str(s))

def tongCacSoNguyenToNhoHonN():
    n = nhapSoNguyenDuong()
    s = 0
    temp = 0
    for i in range(1, n):

        if i == 2:
            temp = 2
        for j in range(2, i):
            if i % j == 0:
                temp = 0
                break
            else:
                temp = i
        s += temp
    return print("Tong cac so nguyen to nho hon " + str(n) + " la: " + str(s))

def tongCacSoChinhPhuong():
    n = nhapSoNguyenDuong()
    s = 0
    for i in range(1, n):
        a = math.modf(math.sqrt(i))
        if a[0] == 0:
            s += i
    return print("Tong cac so chinh phuong nho hon " + str(n) + " la: " + str(s))





