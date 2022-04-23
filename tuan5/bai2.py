def nameInput():
    return str(input("Nhap ho va ten cua ban: "))

def chuanHoaChuoi():
    a = nameInput()
    x = a.rsplit(" ")
    for i in x:
        if i != "":
            print(i.casefold().capitalize(), end=" ")

def xuatTungKiTuLenTungDong():
    a = nameInput()
    for i in a:
        print(i)


def xuatTungChuLenTungDong():
    a = nameInput()
    x = a.rsplit(" ")
    for i in x:
        if i != "":
            print(i.casefold().capitalize())


def xuatTungChuLenTungDongNguocLai():
    a = nameInput()
    x = a.rsplit(" ")
    x.reverse()
    for i in x:
        if i != "":
            print(i.casefold().capitalize())


def xuatTenHoTenLot():
    a = nameInput()
    full_name = []
    x = a.rsplit(" ")
    for i in x:
        if i != "":
            full_name.append(i.casefold().capitalize())
    print("Ten: " + str(full_name[-1]))
    print("Ho: " + str(full_name[0]))
    if len(full_name) != 2:
        print("Ho lot: ", end="")
        full_name.pop(0)
        full_name.pop(-1)
        for i in full_name:
            print(str(i), end="")
