def nhapN():
    n = int(input("Nhap so nguyen duong n: "))
    return n

def tamGiacDac():
    n = nhapN()
    while n >= 1:
        print("*"*n)
        n -= 1
    return 0

def tamGiacRong():
    n = nhapN()
    a = n - 1
    count = -1
    for i in range(1, n + 1):
        if i == 1:
            print(" "*a + "*")
        elif i == n:
            print("*"*(2*n - 1))
        else:
            print(" "*a + "*" + " "*count + "*")
        count += 2
        a -= 1
    return 0