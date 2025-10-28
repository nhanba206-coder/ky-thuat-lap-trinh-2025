print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
def benefit(t, n, k):
    total = n * (1 + t/100) ** k
    return total

t = float(input("Nhập lãi suất hàng tháng (%): "))
n = float(input("Nhập số tiền gửi ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

print("Số tiền nhận được sau", k, "tháng là:", benefit(t, n, k))

