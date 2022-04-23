def inputNumber():
    n = int(input("Nhap n: "))
    arr = []
    for i in range(0, n):
        arr.append(input("Nhap phan tu thu " + str(i + 1) + " : "))
    f = open("input.txt", "a")
    for i in arr:
        f.write(str(i) + "\n")
    f.close()
    return n

def congNhan(n):
    tong = 0
    tich = 1
    f = open("input.txt", "r")
    f2 = open("kq.txt", "a")
    arr1 = []

    for i in range(0, n):
        arr1.append(int(f.readline()))
    # for line in f:
    #     arr1.append(int(line.replace("\n", "")))

    for i in arr1:
        tong += i
        tich *= i
    f2.write(str(tong) + "\n")
    f2.write(str(tich) + "\n")
    f2.write("////////////")


