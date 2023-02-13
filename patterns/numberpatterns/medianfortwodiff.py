from math import ceil


def median(len,array):
    if(len%2==0):
      medium=len//2
      median=(array[medium]+array[medium+1])/2
      return median
    else:
        medium=ceil(len/2)
        return array[medium-1]






a=[2, 10, 12, 26]
b= [3, 6, 30, 78, 90]

a=a+b
a.sort()
ans =median(len(a),a)
print(ans)

