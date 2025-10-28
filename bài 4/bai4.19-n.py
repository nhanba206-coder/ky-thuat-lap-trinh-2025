print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    import math
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:limit+1:p] = b'\x00' * (((limit - start)//p) + 1)
    return [i for i, isprime in enumerate(sieve) if isprime]
P = tuple(primes_upto(1_000_000 - 1))
print("Số lượng số nguyên tố nhỏ hơn 1 triệu:", len(P))
print("10 số nguyên tố đầu:", P[:10])
print("10 số nguyên tố cuối:", P[-10:])
