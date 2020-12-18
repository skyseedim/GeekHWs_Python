a = int(input("\n>> Задание № 4 \nВведите целое число: "))
"""n = len(a) - 1
c = int(a[n])
while n > 0:
    b = c - int(a[n-1])
    if b <= 0:
        c = int(a[n-1])
    n -= 1"""
b = 0
while True:
    c = a % 10
    if c > b:
        b = c
    a = a // 10
    if a == 0:
        break
print(b)
print(f"Самая большая цифра в числе: {b}")
a, b, c = None, None, None
