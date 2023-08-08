def findnextperm(l):
    n=len(l)
    ind=-1
    for i in range(n-2,-1,-1):
        print(l[i],end=" ")

        if(l[i]<l[i+1]):
            ind=i
            break
    if ind==-1:
        l.reverse()
        return l
    for i in range(n-1,ind,-1):
        if(l[i]>l[ind]):
            l[i],l[ind]=l[ind],l[i]
            break
    l[ind+1:]=reversed(l[ind+1:])
    return l
            







if __name__=="__main__":

  l=[2,1,5,4,3,0,0]
  a=findnextperm(l)
  print(a)