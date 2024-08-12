a = [4,5,6,7,8,9,34,5]
max_value = a[0]
for i in range(1, len(a)):
    if (a[i] > max_value):
        max_value = a[i]
print(a.index(max_value))