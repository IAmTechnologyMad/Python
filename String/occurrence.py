string = input("Enter the string")
f = input("Enter the the char")
count = 0

for i in range(len(string)):
    if (string[i] == f):
        count = count + 1
print(count)
        