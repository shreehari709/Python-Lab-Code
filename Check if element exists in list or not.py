lst=[]
n= int(input("Enter the number of elements in list: "))
for x in range(0,n):
    element=int(input("Enter element " + str(x+1) + ": "))
    lst.append(element)
i=int(input("Enter the Number to be Check "))
if i in lst:
    print("exist")
else:
    print("not exist")