print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import my_module

n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

max_val, min_val = my_module.find_max_min(lst)

print("Danh sách:", lst)
print("Phần tử lớn nhất:", max_val)
print("Phần tử nhỏ nhất:", min_val)
