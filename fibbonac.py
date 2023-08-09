def fib(n):
    if n==0 or n==1:
       return 1
       

    #if(n>2):
        
    else:
      return fib(n-1)+fib(n-2)
    




n=5
for i in range(n):
  ans=fib(i)
  print(ans)

