n = str(input("Enter the String = "))
l = ["a", "e", "i", "o", "u"]
# a = "Hello, World!"
s = len(n)
for i in range(0, s):
    n.replace(l[i], "@")
print(n)