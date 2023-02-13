def findpair(pairs):
     s=set()

     for (x,y) in pairs:
        s.add((x,y))

        if(y,x) in s:
          print((x,y))

pairs=[(3,4),(3,5),(4,3),(7,6),(6,7)]
findpair(pairs)
