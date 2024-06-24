print("Enter the Marks of Student ")
m=int(input())
if m>100 and m < 0:
    print("Invalid Marks")
elif m<=100 and m>=90:
    print("Grade = A+")
elif m<90 and m>=80:
    print("Grade = A")
elif m<80 and m>=70:
    print("Grade = A-")
elif m<70 and m>=60:
    print("Grade = B+")
elif m<60 and m>=50:
    print("Grade = B")
elif m<50 and m>=40:
    print("Grade = B-")
elif m<40 and m>=0:
    print("Fail")