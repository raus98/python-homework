def userInputChecker():
    while True:
        try:
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print("a/b = "+ str(a / b))
        except ValueError:
            print("Invalid input!")
        except ZeroDivisionError:
            print("Division by zero")
        else:
            break
