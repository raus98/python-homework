from bai1 import create, showAll, sorter

main_list = []
n = int(input("Nhap so luong nhan vien: "))
create(n, main_list)
showAll(n, main_list)
showAll(n, sorter(n, main_list))


