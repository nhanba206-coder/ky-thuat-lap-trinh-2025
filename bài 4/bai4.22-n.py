print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
res = []
for x in range(1000, 3001):
    s = str(x)
    if all(int(ch) % 2 == 0 for ch in s):
        res.append(s)
print(",".join(res))
