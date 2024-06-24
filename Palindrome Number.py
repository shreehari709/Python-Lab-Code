print("Shreehari Kalundia \nA35404921001")
print("Enter the Number = ")
n=int(input())
a=n
rev = 0
while(n>0):
   # rem=n%10
    rev=(rev*10)+n%10
    n=n//10
if a == rev:
    print("Number is Palindrome")
else:
    print("Number is Not a Palindrome Number")
