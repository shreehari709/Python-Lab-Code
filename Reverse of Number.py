print("Shreehari Kalundia \nA35404921001")

n=int(input("Enter the Number = "))
rev = 0
while(n>0):
    #rem=n%10
    rev=(rev*10)+n%10
    n=n//10

print("Reverse of Number = "+ str(rev))

        