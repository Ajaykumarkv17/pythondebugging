
students=[["chi",34],["Ajay",34],["aswin",47]]
scores=list(set([students[i][1] for i in range(3)]))
scores.sort()
SecondLow=scores[1]
SecondLowStudents=[students[i][0] for i in range(3) if students[i][1]==SecondLow]
SecondLowStudents.sort()
for S in SecondLowStudents:
    print(S)