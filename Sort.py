'''
f=open("demofile.txt","a")
f.write("\nHello New Line")
f.close()
f=open("demofile.txt","r")
print(f.read())
'''
try:
    x = int(input())
except  Exception as e:
    print("error",e)
