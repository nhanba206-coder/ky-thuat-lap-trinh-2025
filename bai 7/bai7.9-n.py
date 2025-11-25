
print("Sinh viên: Nguyễn Bá Nhàn - MSV: 245752021610141")
print("Bài 9 - Sao chép file")
print("="*50)
open("copy.txt","w",encoding="utf-8").write(open("test.txt",encoding="utf-8").read())
print("Đã sao chép test.txt → copy.txt")
