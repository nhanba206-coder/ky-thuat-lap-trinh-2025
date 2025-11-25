
print("Sinh viên: Nguyễn Bá Nhàn - MSV: 245752021610141")
print("Bài 2 - Đếm dòng, từ, ký tự"); print("="*50)
lines = words = chars = 0
with open("test.txt", encoding="utf-8") as f:
    for line in f:
        lines += 1
        chars += len(line)
        words += len(line.split())
print(f"Dòng: {lines} | Từ: {words} | Ký tự: {chars}")
