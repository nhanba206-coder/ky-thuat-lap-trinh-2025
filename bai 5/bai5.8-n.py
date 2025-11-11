print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import search_module as sm  

numbers = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]

target = int(input("Nhập số cần tìm: "))
index = sm.linear_search(numbers, target)

if index != -1:
    print(f"Tìm thấy {target} tại vị trí {index}")
else:
    print(f"Không tìm thấy {target} trong danh sách")

index2 = sm.binary_search(numbers, target)
print(f"(Tìm kiếm nhị phân) Kết quả: {index2}")
