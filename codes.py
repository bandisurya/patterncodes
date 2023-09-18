# Q)For finding ascii values
# A-Z=65-90
# a-z=97-122
# 0-9=48-57
a=input()
b=ord(a)
if 65<=b<=90:#for capital letters 
    print("1")
elif 97<=b<=122:#for small letters
    print("0")
else:
    print("-1")

