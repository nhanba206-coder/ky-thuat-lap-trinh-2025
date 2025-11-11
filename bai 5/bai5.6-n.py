print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import numpy as np

arr = np.array([12, 15, 7, 34, 25, 9, 38, 14, 30])
print("Mảng ban đầu:")
print(arr)
max_value = np.max(arr)
min_value = np.min(arr)

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print(f"Phần tử lớn nhất là {max_value}, tại vị trí {max_index}")
print(f"Phần tử nhỏ nhất là {min_value}, tại vị trí {min_index}")
