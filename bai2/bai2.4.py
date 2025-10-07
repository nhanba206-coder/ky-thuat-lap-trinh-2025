a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

for n in range(a + 1, b):
    inverse = 1 / n
    print(f"Nghịch đảo của {n} là: {inverse}")
