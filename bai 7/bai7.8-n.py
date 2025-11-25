
print("Sinh viên: Nguyễn Bá Nhàn - MSV: 245752021610141")
print("Bài 8 - Ghi danh sách")
print("="*50)
colors = ["Red","Green","White","Black","Pink","Yellow"]
open("colors.txt","w",encoding="utf-8").write("\n".join(colors))
print("Đã tạo colors.txt")
