print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
s = input("Nhập các số, phân tách bằng dấu phẩy: ")
nums = [int(x.strip()) for x in s.split(',') if x.strip()]
odds = [str(x) for x in nums if x % 2 == 1]
print(",".join(odds))
