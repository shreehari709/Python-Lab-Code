def fib(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return (fib(num - 1) + fib(num - 2))
n = int(input())
print("Fibonacci series:", end = ' ')
for n in range(0, n):
   print(fib(n), end = ' ')