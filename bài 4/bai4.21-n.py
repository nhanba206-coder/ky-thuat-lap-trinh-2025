print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
s = input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
items = [x.strip() for x in s.split(',') if x.strip()]
res = [x for x in items if len(x)==4 and int(x, 2) % 5 == 0]
print(",".join(res))
