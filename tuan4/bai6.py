def nameInput():
    name = str(input("Nhap ho va ten: "))
    return name

def characterPerLine():
    a = nameInput()
    for i in a:
        print(i)
    return 0

def wordPerLine():
    a = nameInput()
    for i in a:
        if i != " ":
            print(i)
    return 0

def reverseWordPerLine():
    a = nameInput()
    for i in a[::-1]:
        if i != " ":
            print(i)
    return 0

def numberOfNamePartsPerLine():
    a = nameInput()
    for i in a:
        if i != " ":
            print(i, end="")
        else:
            print()
    return 0



