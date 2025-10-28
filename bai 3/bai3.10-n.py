print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ!")
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R * R
        print("Chu vi =", chu_vi)
        print("Diện tích =", dien_tich)

R = float(input("Nhập bán kính R: "))
Tinh(R)
