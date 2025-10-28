print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import sys
lines = []
print("Nhập các giao dịch (ví dụ 'D 300'), mỗi giao dịch 1 dòng. Nhấn Enter rỗng để kết thúc:")
while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        break
    lines.append(line)
balance = 0
for line in lines:
    parts = line.split()
    if len(parts) != 2:
        continue
    typ, amt = parts[0].upper(), float(parts[1])
    if typ == 'D':
        balance += amt
    elif typ == 'W':
        balance -= amt
if balance.is_integer():
    print(int(balance))
else:
    print(balance)
    
