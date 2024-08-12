def rep(arr, n): 
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (rep[i] != rep[j]):
                return 






if __name__ == '__main__':
  arr = [7,7,10, 5, 3, 4, 3, 5, 6]
  n = len(arr)
  
  index =   rep(arr,n)
  
  if index == -1:
      print("not found")
  else:
      print(arr[index])