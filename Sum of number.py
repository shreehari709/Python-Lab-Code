print("Enter the Number")
n=int(input())
new=0
while(n>0):
    s=int(n%10)
    new=new+s
    n=n/10
print("Sum of Number = ",new)
    