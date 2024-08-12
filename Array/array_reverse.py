# A - array, size - size of the array, X - target element
def pair(A, size, X):
    for i in range(0, size - 1):
        for j in range(i+1, size):
            if (A[i] + A[j] == X):
                return 1
    return 0
    



if __name__ == "__main__":
    A = [1,2,3,4,6]
    size = len(A)
    X = 9

    if (pair(A, size, X)):
        print("found")
    else:
        print("Not found")
