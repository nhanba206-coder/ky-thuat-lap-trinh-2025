print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
lst = input("Nhập list: ").split()
x = input("Phần tử muốn bỏ: ")
lst = [item for item in lst if item != x]
print(lst)
