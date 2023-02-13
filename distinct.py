
from itertools import count


def countFreq(arr, n):

  
   visited = [False for i in range(n)]
   count=0

   for i in range(n):

    
     if (visited[i] == True):
        continue


     
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
     count += 1

   print(count)


arr = [10, 30, 10, 20, 10, 20, 30, 10,46,44,44]
n = len(arr)
countFreq(arr, n) 