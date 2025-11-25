print("Sinh viên: Nguyễn Bá Nhàn - MSV: 245752021610141")
print("Bài 6 - Đọc n dòng cuối")
print("="*50)
n = int(input("Nhập số dòng cuối cần đọc: "))
lines = open("test.txt", encoding="utf-8").readlines()
for line in lines[-n:]:
    print(line.strip())
