print("Sinh viên: Nguyễn Bá Nhàn")
print("MSV: 245752021610141")
print("Bài 5 - Đảo ngược từng từ")
print("-" * 35)

class ReverseWords:
    def reverse_string(self):
        text = input("Nhập chuỗi: ")
        words = text.split()
        print("Kết quả:", " ".join(word[::-1] for word in words))

ReverseWords().reverse_string()
