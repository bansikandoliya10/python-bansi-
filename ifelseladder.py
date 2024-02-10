m1=int(input("enter markes1: "))
m2=int(input("enter markes2: "))
m3=int(input("enter markes3: "))

if m1>=28 and m2>=28 and m3>28:
    total=m1+m2+m3
    per=total/3
    result="PASS"
    if per>=80:
        grade="A"
    elif per>=70:
        grade="B"
    elif per>=60:
        grade="C"
    else:
        grade="D"
        
else:
    total=m1+m2+m3
    per="***"
    result="FAIL"
    grade="F"
        
print("total: ", total)
print("percentage: ", per)
print("result: ", result)
print("grade: ")
    