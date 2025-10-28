print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
fullname = input("Nhập họ và tên: ").strip()
parts = fullname.split()
if len(parts) >= 2:
    ho = parts[0]
    ten = parts[-1]
    print("Họ:", ho)
    print("Tên riêng:", ten)
else:
    print("Dữ liệu nhập không hợp lệ (cần có ít nhất họ và tên).")
