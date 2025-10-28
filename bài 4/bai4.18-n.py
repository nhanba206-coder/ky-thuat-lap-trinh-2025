print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
n = int(input("Nhập n: "))
fib = []
a, b = 0, 1
while a < n:
    fib.append(a)
    a, b = b, a + b
print(fib)
