def check(piles,ind,h):
  time=0
  for i in range(len(piles)):
    if(piles[i]%ind!=0):
        time=time+((piles[i]//ind)+1)
    else:
        time=time+(piles[i]//ind)

  if(time<=h):
    return True
  else:
    return False

def minimumtime(piles,h):
    start=0
    end=sorted(piles.copy(),reverse=True)[0]
    
    while(start<end):
        mid=(start+end)//2
        if(check(piles,mid,h)==True):
                end=mid
        else:
            start=mid+1
    

    return end







piles=[30,11,23,4,20]
h=6
print("The minimum time is",minimumtime(piles,h))
