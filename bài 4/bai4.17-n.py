print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
def sum_proper_divisors(x):
    if x <= 1:
        return 0
    s = 1
    i = 2
    import math
    while i * i <= x:
        if x % i == 0:
            s += i
            j = x // i
            if j != i:
                s += j
        i += 1
    return s

n = int(input("Nhập n: "))
res = [i for i in range(1, n) if sum_proper_divisors(i) > i]
print(res)
