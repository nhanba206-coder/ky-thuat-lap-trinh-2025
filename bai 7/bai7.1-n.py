print("Sinh viên: Nguyễn Bá Nhàn - MSV: 245752021610141")
ten_file = input("Nhập tên file : ")
try:
    with open(ten_file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip()[::-1])
except FileNotFoundError:
    print("Không tìm thấy file!.")
