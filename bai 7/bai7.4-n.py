print("Sinh viên: Nguyễn Bá Nhàn")
print("MSV: 245752021610141")
print("Bài 4 - Đọc n dòng đầu tiên")
print("="*50)

n = int(input("Nhập số dòng cần đọc: "))
with open('test.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < n:
            print(line.strip())
        else:
            break
