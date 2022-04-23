def cauA():
    a = input("Nhap a: ")
    b = input("Nhap b: ")
    f = open("input.txt", "a")

    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.close()

def cauB():
    f = open("input.txt", "r")
    f2 = open("kq.txt", "a")
    arr = []
    for line in f:
        arr.append(int(line.replace("\n", "")))

    f2.write(str(arr[0] + arr[1]) + "\n")
    f2.write(str(arr[0] * arr[1]) + "\n")
