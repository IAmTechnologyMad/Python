test = input("Enter the string")
vowels = ['a','e','i','o','u']
for i in range(len(test)):
    if (test[i] in vowels):
        print("vowels")
    else:
        print("no")