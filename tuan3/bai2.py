def tinhTong(n):
    soChan = 0
    soLe = 0
    s = -1
    for i in range(1, n+1):
        soChan = soChan + 2*i
        soLe = soLe + 2*i - 1
        s = s + soChan/soLe
    return print("Bai tap 2: s = " + str(s))

