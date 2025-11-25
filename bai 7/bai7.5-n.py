print("Sinh viên: Nguyễn Bá Nhàn")
print("MSV: 245752021610141")
print("Bài 5 - Ghi văn bản vào tệp")
print("="*50)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Python Exercises\n")
    f.write("Java Exercises\n")
    f.write("C++ Programming\n")

print("Đã ghi thành công vào output.txt")
with open('output.txt', 'r', encoding='utf-8') as f:
    print("Nội dung file vừa tạo:")
    print(f.read())
