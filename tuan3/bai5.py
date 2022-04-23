import datetime

def getWeekDay():
    dd = int(input("Ngày: "))
    mm = int(input("Tháng: "))
    yyyy = int(input("Năm: "))
    current_day = datetime.datetime(yyyy, mm, dd)
    return print(str(dd) + "/" + str(mm) + "/" + str(yyyy) + ": " + changeEng2Vi(current_day.strftime("%A")))

def changeEng2Vi(i):
    switcher = {
        "Monday": "Thứ hai",
        "Tuesday": "Thứ ba",
        "Wednesday": "Thứ tư",
        "Thursday": "Thứ năm",
        "Friday": "Thứ sáu",
        "Saturday": "Thứ bảy",
        "Sunday": "Chủ nhật"
    }
    return switcher.get(i, "Something went wrong")
