n = 9
a = 1
b = 0
for i in range(0, n):
    c = a + b
    a = b
    b = c
    print(b)