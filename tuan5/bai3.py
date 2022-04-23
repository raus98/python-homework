def checkAllConditions():
    pass_word = passwordInputListCharacters()
    if checkChuCaiThuong(pass_word) and checkChuSo(pass_word) and checkChuCaiHoa(pass_word) and checkKiTuDacBiet(pass_word) and checkMaxCharacters(pass_word) and checkMinCharacters(pass_word):
        return print("Mật khẩu hợp lệ!")
    return print("Mật khẩu không hợp lệ :v")

def passwordInputListCharacters():
    return list(str(input("Nhap mat khau: ")))

def checkChuCaiThuong(x):
    for i in x:
        if str(i).isalpha():
            return True
    return False

def checkChuSo(x):
    for i in x:
        if str(i).isnumeric():
            return True
    return False

def checkChuCaiHoa(x):
    for i in x:
        if str(i).isupper():
            return True
    return False

def checkKiTuDacBiet(x):
    count = 0
    for i in x:
        if not str(i).isnumeric() and not str(i).isalpha():
            return True
    return False

def checkMinCharacters(x):
    if len(x) >= 6:
        return True
    return False

def checkMaxCharacters(x):
    if len(x) <= 12:
        return True
    return False
