import math

class Circle:
    def __init__(self, ban_kinh):
        self.r = ban_kinh

    def dien_tich(self):
        return math.pi * self.r ** 2

    def chu_vi(self):
        return 2 * math.pi * self.r

print("CHƯƠNG TRÌNH TÍNH DIỆN TÍCH & CHU VI HÌNH TRÒN")
print("=" * 45)

r = float(input("Nhập bán kính hình tròn: "))

hinh_tron = Circle(r)                    

print(f"Diện tích = {hinh_tron.dien_tich():.2f}")
print(f"Chu vi    = {hinh_tron.chu_vi():.2f}")
