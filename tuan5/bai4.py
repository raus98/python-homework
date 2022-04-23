
def dictionary(dict):
    print("             MY DICTIONARY                      ")
    print("**************** MENU **************************")
    print("**   1. Thêm từ          4. Liệt kê tất cả    **")
    print("**   2. Xóa từ           5. Tra từ            **")
    print("**   3. Sửa từ           0. Thoát             **")
    print("************************************************")
    try:
        menuSelection(int(input(" ")), dict)
    except:
        print()
        print("Pls input again!")
        print()
        dictionary(dict)
    return 0

def menuSelection(x, dict):
    if x == 1:
        addWords(dict)
    elif x == 2:
        deleteWords(dict)
    elif x == 3:
        fixWords(dict)
    elif x == 4:
        enumerate(dict)
    elif x == 5:
        findWords(dict)
    elif x == 0:
        return False
    else:
        print()
        print("WTF input, pls try again")
        print()
    return dictionary(dict)

def addWords(dict):
    print(">>>>> Thêm từ mới <<<<<")
    x = str(input("Eng: "))
    y = str(input("Vie: "))
    dict.update({x: y})
    print()
    print('"' + x + " => " + y + '" has been added')
    print()
    return 0

def deleteWords(dict):
    b = str(input("Nhập từ cần xóa(ENG): "))
    print()
    print('"' + b + " => " + str(dict.get(b)) + '" has been deleted')
    print()
    try:
        dict.pop(b)
    except:
        print("Opps! May be your word not in my dictionary")
        print("Pls try again!")
        print()
    return 0

def fixWords(dict):
    b = str(input("Nhập từ cần sửa(ENG): "))
    if b not in dict:
        print("Your word is not in my dictionary")
        return 0
    c = str(dict.get(b))
    dict[b] = str(input(b + " => "))
    print()
    print('"' + b + " => " + c + '" has been changed to ' + '"' + b + " => " + str(dict.get(b) + '"'))
    print()
    return 0

def findWords(dict):
    b = str(input("Nhập từ cần tra(ENG): "))
    print()
    if dict.get(b) == None:
        print("Your word is not in my dictionary")
    else:
        print('"' + b + " => " + str(dict.get(b)) + '"')
    print()
    return 0

def enumerate(dict):
    print()
    for k, v in dict.items():
        print(k, "=>", v)
    print()
    return 0
