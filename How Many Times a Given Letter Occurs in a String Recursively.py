def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)

str=input("Enter the String = ")
#string = raw_input("Enter string:")
ch=input("Enter the character to Check = ")
#ch = raw_input("Enter character to check:")
print("Count is:")
print(check(str, ch))