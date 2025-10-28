print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
def pascal(n):
    row = [1]
    for _ in range(n):
        print(' '.join(map(str, row)))
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

n = int(input("Nhập n: "))
pascal(n)
