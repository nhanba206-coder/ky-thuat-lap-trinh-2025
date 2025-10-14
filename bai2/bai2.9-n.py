print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
s = input("Nhập vào một chuỗi: ")
char_count = {}
for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print(char_count)
