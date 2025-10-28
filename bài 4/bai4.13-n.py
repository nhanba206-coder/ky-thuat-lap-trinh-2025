print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
lst = input("Nhập list: ").split()
x = input("Phần tử cần tìm: ")
positions = [i for i, val in enumerate(lst) if val == x]
if positions:
    print("Tìm thấy tại vị trí (0-based):", positions)
else:
    print("Không tìm thấy")
