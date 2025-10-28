print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
line = input("Nhập các từ: ")
words = line.split()
if not words:
    print("Không có từ")
else:
    maxlen = max(len(w) for w in words)
    longest = [w for w in words if len(w) == maxlen]
    print(" ".join(longest))
