print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
a, b = 1, 2
total = 0
print(a, end=" ")
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
    print(a, end=" ")
print("\nTổng các số chẵn trong dãy Fibonacci là:", total)
