def soLonNhat(mang):
    max_value = 0
    for i in mang:
        if max_value < i:
            max_value = i
    return print("So lon nhat: " + str(max_value))

def soLonNhi(mang):
    mang.sort()
    max_value = max(mang, default=99)
    try:
        second_max = mang[len(mang) - mang.count(max_value) - 1]
        a = "So lon nhi: " + str(second_max)
    except:
        a = "Empty Lists"
    return print(a)

def kiemTraMangDoiXung(mang):
    i = 0
    n = int(len(mang) / 2)
    for i in range(0, n):
        if mang[i] != mang[len(mang) - i - 1]:
            return print("Mang khong doi xung")
    return print("Mang doi xung")

def tongSoNguyenTo(mang):
    S = 0
    temp = 0
    for i in mang:
        if i == 2:
            S += i
        else:
            for n in range(1, i):
                if n == 1:
                    continue
                if i % n == 0:
                    temp = 0
                    break
                else:
                    temp = i
            S += temp
            temp = 0
    return print("Tong cac so nguyen to: " + str(S))

def cacPhanTuLonHonX(mang):
    x = int(input("Nhap x: "))
    xyz = []
    for i in mang:
        if i > x and i not in xyz:
            xyz.append(i)
    return print("Cac phan tu lon hon X: " + str(xyz))

def sapXepMangTangDan(mang):
    mang.sort()
    return print("Sap xep mang tang dan: " + str(mang))