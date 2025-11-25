
print("Sinh viên: Nguyễn Bá Nhàn")
print("MSV: 245752021610141")
print("Bài 3 - Đọc toàn bộ tệp")
print("="*50)

with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
