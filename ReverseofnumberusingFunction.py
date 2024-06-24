def rev(n):
    rev = 0
    while (n > 0):
        rev = (rev * 10) + n % 10
        n = n // 10
    print("Reverse of Number = " + str(rev))
n=int(input("Enter the Number = "))
rev(n)

